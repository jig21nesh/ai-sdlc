#!/usr/bin/env python3
"""Validate the portable pack's references and declared source-practice coverage.

This checks integrity, not semantic correctness or runtime enforcement.
"""
import json
import re
from pathlib import Path
from build import source_catalog

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text())


def check():
    manifest = read('skills/manifest.json')
    inventory = read('research/playbook-inventory.json')
    skills = manifest['skills']
    errors = []
    paths = {str(p.relative_to(ROOT)) for p in (ROOT / 'skills').glob('*/SKILL.md')}
    if paths != {s['path'] for s in skills} or len({s['id'] for s in skills}) != len(skills):
        errors.append('Skill manifest does not match unique skill directories')
    practices = {p['id'] for p in inventory['items']}
    covered = {p for s in skills for p in s['practice_ids']}
    if practices != covered:
        errors.append(f'Practice mismatch: missing={sorted(practices-covered)}, unknown={sorted(covered-practices)}')
    sources = {key for s in source_catalog() for key in [s['id'], *s.get('aliases', [])]}
    profiles = {'org': read('config/org.example.json'), 'project': read('config/project.example.json')}
    for s in skills:
        p = ROOT / s['path']
        if not p.is_file():
            continue
        text = p.read_text()
        if not text.startswith('---\n') or not re.search(r'^name: ' + re.escape(s['id']) + r'$', text, re.M):
            errors.append(f'{s["id"]}: frontmatter name mismatch')
        if not set(s['evidence_ids']) <= sources:
            errors.append(f'{s["id"]}: unresolved evidence')
        for output in s['output_templates']:
            if not (ROOT / output).is_file():
                errors.append(f'{s["id"]}: missing output template')
        for path in s['organization_fields'] + s['project_fields']:
            keys = path.split('.')
            node = profiles
            try:
                for key in keys:
                    node = node[key]
            except (KeyError, TypeError):
                errors.append(f'{s["id"]}: unknown profile path {path}')
    for p in inventory['items']:
        for edge in p['upstream']:
            if edge['id'] not in practices or edge['requirement'] not in ('required', 'advisory', 'conditional'):
                errors.append(f'{p["id"]}: invalid inventory edge')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(skills)} skills cover {len(practices)} inventoried practices; sources, templates and configuration paths resolve.')
    print('Integrity only: this does not establish skill selection, decision quality or enforced runtime controls.')
    return 0


if __name__ == '__main__':
    raise SystemExit(check())
