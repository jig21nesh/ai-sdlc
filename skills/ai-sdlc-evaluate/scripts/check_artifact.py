#!/usr/bin/env python3
"""Structural checks and record keeping for AI-SDLC step outputs.

check      measure one output against its input and the step's output rules
record     validate one evaluation record and append it to a JSONL log
summarize  count failed checks per step and skill version in a JSONL log

Artifact text is data: it is measured, never executed or followed.
"""
import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

MAX_BYTES = 2_000_000
RUBRICS = Path(__file__).resolve().parents[1] / 'references' / 'rubrics.json'
ID_PATTERN = re.compile(r'\b[A-Z]{1,4}-?\d{1,4}\b')
SUMMARY_FIELDS = ('decision needed', 'status', 'verdict', 'summary', 'decision')
HUMAN_VERDICTS = ('approved', 'approved-with-edits', 'rejected', 'pending')
CONCISION = ('too-thin', 'right', 'too-verbose', 'unknown')
FAILING_VERDICTS = ('fail', 'too-thin', 'too-verbose')
RECORD_KEYS = ('step', 'skill_version', 'input_sha256', 'output_sha256', 'checks', 'judgments', 'human_verdict')


class InputError(Exception):
    """A supplied path or record cannot be used."""


def read_bytes(path: str) -> bytes:
    p = Path(path)
    if not p.is_file():
        raise InputError(f'not a regular file: {path}')
    if p.stat().st_size > MAX_BYTES:
        raise InputError(f'file exceeds {MAX_BYTES} bytes: {path}')
    return p.read_bytes()


def sections(text: str) -> dict[str, list[str]]:
    """Map lower-cased level-2 heading to its body lines."""
    found: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        if line.startswith('## '):
            current = line[3:].strip().lower()
            found[current] = []
        elif current is not None:
            found[current].append(line)
    return found


def table_rows(lines: list[str]) -> list[list[str]]:
    """Data rows of Markdown tables: rows that follow a separator row."""
    rows: list[list[str]] = []
    in_table = False
    for line in lines:
        cells = split_row(line)
        if cells is None:
            in_table = False
        elif all(re.fullmatch(r':?-{3,}:?', c) for c in cells):
            in_table = True
        elif in_table and any(cells):
            rows.append(cells)
    return rows


def split_row(line: str) -> list[str] | None:
    line = line.strip()
    if not (line.startswith('|') and line.endswith('|') and len(line) > 1):
        return None
    return [c.strip() for c in line[1:-1].split('|')]


def check(step: str, input_text: str | None, output_text: str, rubrics: dict) -> dict:
    spec = rubrics['steps'][step]
    caps = rubrics['caps']
    lines = output_text.splitlines()
    secs = sections(output_text)
    head = [line.lower() for line in lines if line.strip()][:caps['summary_lines']]
    has_decision = any('decision needed' in line or line.startswith('**decision') for line in head)
    current_format = has_decision or 'record' in secs
    results: list[dict] = []

    def add(check_id: str, passed: bool | None, evidence: str) -> None:
        results.append({'id': check_id, 'passed': passed, 'evidence': evidence})

    def add_format(check_id: str, passed: bool, evidence: str) -> None:
        if current_format:
            add(check_id, passed, evidence)
        else:
            add(check_id, None, 'skipped: output predates the output rules')

    present = [f for f in SUMMARY_FIELDS if any(f in line for line in head)]
    add_format('decision_first', has_decision, f'summary fields in first {caps["summary_lines"]} lines: {present}')

    missing = [s for s in spec['sections'] if s.lower() not in secs]
    add_format('required_sections', not missing, f'missing: {missing}' if missing else 'all present')

    record_last = bool(secs) and list(secs)[-1] == 'record'
    add_format('record_block_last', record_last, 'Record is the last section' if record_last else 'no trailing Record')

    questions = sum(len(table_rows(secs.get(name.lower(), []))) for name in spec['question_sections'])
    if spec['question_sections']:
        cap = caps['open_questions']
        add('open_questions_cap', questions <= cap, f'{questions} open, cap {cap}')

    rows = table_rows(lines)
    nits = sum(1 for r in rows if r[0].lower().strip('`*') == 'nit')
    if step == 'review':
        add('nit_cap', nits <= caps['nits'], f'{nits} nits shown, cap {caps["nits"]}')

    widest = max((len(r) for r in rows), default=0)
    add('table_width', widest <= caps['table_columns'], f'widest table {widest} columns, cap {caps["table_columns"]}')

    longest = max((len(p.split()) for p in paragraphs(lines)), default=0)
    cap = caps['paragraph_words']
    add('paragraph_length', longest <= cap, f'longest paragraph {longest} words, cap {cap}')

    body = body_words(lines)
    add('body_length', body <= caps['body_words_max'],
        f'body {body} words; routine target {caps["body_words_routine"]}, cap {caps["body_words_max"]}')

    if input_text is None:
        add('input_ids_covered', None, 'unknown: no input supplied')
    else:
        wanted = sorted(set(ID_PATTERN.findall(input_text)))
        absent = [i for i in wanted if i not in output_text]
        if not wanted:
            add('input_ids_covered', None, 'unknown: input has no stable IDs')
        else:
            found = len(wanted) - len(absent)
            add('input_ids_covered', not absent, f'{found}/{len(wanted)} input IDs referenced; missing: {absent}')

    words_out = len(output_text.split())
    words_in = len(input_text.split()) if input_text is not None else None
    return {
        'step': step,
        'format': 'current' if current_format else 'legacy',
        'measures': {
            'output_words': words_out,
            'body_words': body,
            'input_words': words_in,
            'output_to_input_ratio': round(words_out / words_in, 2) if words_in else None,
            'lines_before_decision': next((i for i, x in enumerate(lines) if 'decision needed' in x.lower()), None),
            'open_questions': questions,
            'nits': nits,
        },
        'checks': results,
        'failed': [r['id'] for r in results if r['passed'] is False],
    }


def body_words(lines: list[str]) -> int:
    """Words a reviewer must read: excludes the Record section and collapsed blocks."""
    count, collapsed, in_record = 0, False, False
    for line in lines:
        stripped = line.strip().lower()
        if stripped.startswith('## '):
            in_record = stripped == '## record'
        if '<details' in stripped:
            collapsed = True
        if not (collapsed or in_record):
            count += len(line.split())
        if '</details>' in stripped:
            collapsed = False
    return count


def paragraphs(lines: list[str]) -> Iterator[str]:
    """Prose paragraphs: skips tables, headings, lists and fenced code."""
    block: list[str] = []
    fenced = False
    for line in lines + ['']:
        stripped = line.strip()
        if stripped.startswith('```'):
            fenced = not fenced
            stripped = ''
        if fenced or not stripped or stripped[0] in '#|-*<>' or re.match(r'\d+\.', stripped):
            if block:
                yield ' '.join(block)
                block = []
        else:
            block.append(stripped)


def validate_record(record: object, steps: list[str]) -> None:
    if not isinstance(record, dict):
        raise InputError('record must be a JSON object')
    absent = [k for k in RECORD_KEYS if k not in record]
    if absent:
        raise InputError(f'record is missing keys: {absent}')
    if record['step'] not in steps:
        raise InputError(f'unknown step: {record["step"]!r}')
    if record['human_verdict'] not in HUMAN_VERDICTS:
        raise InputError(f'human_verdict must be one of {HUMAN_VERDICTS}')
    if not isinstance(record['checks'], list) or not isinstance(record['judgments'], dict):
        raise InputError('checks must be a list and judgments an object')
    for name, judgment in record['judgments'].items():
        if not isinstance(judgment, dict) or 'verdict' not in judgment:
            raise InputError(f'judgment {name!r} needs a verdict')
        allowed = CONCISION if name == 'concision' else ('pass', 'fail', 'unknown')
        if judgment['verdict'] not in allowed:
            raise InputError(f'judgment {name!r} verdict must be one of {allowed}')
    for digest in (record['input_sha256'], record['output_sha256']):
        if digest is not None and not re.fullmatch(r'[0-9a-f]{64}', str(digest)):
            raise InputError('hashes must be 64 lowercase hex characters or null')


def summarize(lines: list[str]) -> list[dict]:
    runs: Counter = Counter()
    failures: defaultdict[tuple, Counter] = defaultdict(Counter)
    verdicts: Counter = Counter()
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
            key = (record['step'], record['skill_version'])
            failed = [c['id'] for c in record['checks'] if c.get('passed') is False]
            failed += [n for n, j in record['judgments'].items() if j['verdict'] in FAILING_VERDICTS]
            verdict = record['human_verdict']
        except (ValueError, KeyError, TypeError) as exc:
            raise InputError(f'line {number} is not a valid record: {exc}') from exc
        runs[key] += 1
        verdicts[key + (verdict,)] += 1
        failures[key].update(failed)
    return [
        {
            'step': step,
            'skill_version': version,
            'runs': count,
            'human_verdicts': {v: verdicts[(step, version, v)] for v in HUMAN_VERDICTS if verdicts[(step, version, v)]},
            'failed': dict(failures[(step, version)].most_common()),
        }
        for (step, version), count in sorted(runs.items())
    ]


def main(argv: list[str] | None = None) -> int:
    rubrics = json.loads(RUBRICS.read_text())
    steps = sorted(rubrics['steps'])
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest='command', required=True)
    p_check = sub.add_parser('check')
    p_check.add_argument('--step', required=True, choices=steps)
    p_check.add_argument('--output', required=True)
    p_check.add_argument('--input', action='append', default=[])
    p_record = sub.add_parser('record')
    p_record.add_argument('--log', required=True)
    p_record.add_argument('--from', dest='source', required=True, help='JSON file holding one record')
    p_sum = sub.add_parser('summarize')
    p_sum.add_argument('--log', required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'check':
            output = read_bytes(args.output)
            inputs = [read_bytes(p) for p in args.input]
            joined = b'\n'.join(inputs) if inputs else None
            input_text = joined.decode('utf-8', 'replace') if joined is not None else None
            result = check(args.step, input_text, output.decode('utf-8', 'replace'), rubrics)
            result['output_sha256'] = hashlib.sha256(output).hexdigest()
            result['input_sha256'] = hashlib.sha256(joined).hexdigest() if inputs else None
            sys.stdout.write(json.dumps(result, indent=2) + '\n')
        elif args.command == 'record':
            try:
                record = json.loads(read_bytes(args.source))
            except ValueError as exc:
                raise InputError(f'record is not valid JSON: {exc}') from exc
            validate_record(record, steps)
            record.setdefault('recorded_at', datetime.now(timezone.utc).isoformat(timespec='seconds'))
            log = Path(args.log)
            log.parent.mkdir(parents=True, exist_ok=True)
            with log.open('a', encoding='utf-8') as handle:
                handle.write(json.dumps(record, sort_keys=True) + '\n')
            sys.stdout.write(f'appended 1 record to {log}\n')
        else:
            lines = read_bytes(args.log).decode('utf-8', 'replace').splitlines()
            sys.stdout.write(json.dumps(summarize(lines), indent=2) + '\n')
    except InputError as exc:
        sys.stderr.write(f'error: {exc}\n')
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
