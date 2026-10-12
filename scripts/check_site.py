#!/usr/bin/env python3
"""Check local guide integrity without a browser or third-party packages."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.assets = []
        self.errors = []
        self.scripts = 0
        self.csp = False
        self.h1 = 0
        self.in_script = False
        self.searches = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if 'data-search' in attrs:
            self.searches[attrs.get('id')] = attrs['data-search']
        if tag == 'h1':
            self.h1 += 1
        if any(k.startswith('on') for k in attrs):
            self.errors.append(f'Inline event handler on {tag}')
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'content-security-policy':
            self.csp = True
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag == 'img':
            if not attrs.get('alt'):
                self.errors.append('Missing explanatory alt text')
            for name in ('src', 'data-gif', 'data-still'):
                if attrs.get(name):
                    self.assets.append(attrs[name])
        if tag == 'script':
            self.in_script = True
            self.scripts += 1
            if not attrs.get('src'):
                self.errors.append('Inline script')
            else:
                self.assets.append(attrs['src'])
        if tag == 'link' and 'href' in attrs:
            self.assets.append(attrs['href'])

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False

    def handle_data(self, data):
        if self.in_script and data.strip():
            self.errors.append('Executable inline content')


def check():
    page = Page()
    page.feed((ROOT / 'index.html').read_text())
    errors = page.errors
    if len(set(page.ids)) != len(page.ids):
        errors.append('Duplicate HTML IDs')
    if not page.csp or page.h1 != 1:
        errors.append('Missing CSP or invalid main heading count')
    for link in page.links + page.assets:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            if link in page.assets:
                errors.append(f'Nonlocal automatic asset: {link}')
            elif parsed.scheme != 'https':
                errors.append(f'Unexpected link scheme: {link}')
            continue
        if parsed.path:
            path = (ROOT / unquote(parsed.path)).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                errors.append(f'Missing/outside local file: {link}')
        if not parsed.path and parsed.fragment and unquote(parsed.fragment) not in page.ids:
            errors.append(f'Unresolved fragment: {link}')

    stages = json.loads((ROOT / 'data/stages.json').read_text())
    reference = json.loads((ROOT / 'data/reference-model.json').read_text())
    phases = reference['stages']
    if [phase['name'] for phase in phases] != ['Plan','Design','Build','Test','Deploy','Maintain']:
        errors.append('Reference boxes differ from the reviewed Anthropic stage labels')
    grouped = [m for phase in phases for m in phase['modules']] + reference['cross_cutting'] + reference['extensions']
    if len(grouped) != len(set(grouped)) or set(grouped) != {s['id'] for s in stages}:
        errors.append('Work modules are missing, duplicated or unclassified in the reference mapping')
    if phases[0]['modules'] != ['discover'] or 'plan' not in phases[2]['modules']:
        errors.append('Initial intent and implementation planning have been conflated')
    sources = json.loads((ROOT / 'research/evidence.json').read_text())
    mapping = json.loads((ROOT / 'data/evidence-map.json').read_text())
    ids = {s['id'] for s in sources}
    if len(ids) != len(sources) or len(stages) != 12:
        errors.append('Duplicate evidence or missing lifecycle coverage')
    for stage in stages:
        if not set(mapping.get(stage['id'], [])) <= ids or not mapping.get(stage['id']):
            errors.append(f'Unresolved evidence map: {stage["id"]}')
        if f'stage-{stage["id"]}' not in page.ids:
            errors.append(f'Missing rendered stage: {stage["id"]}')
    for s in sources:
        if f'source-{s["id"]}' not in page.ids:
            errors.append(f'Missing rendered evidence: {s["id"]}')
        for inspected in s.get('inspected_files', []):
            if inspected['url'] not in page.links:
                errors.append(f'Missing inspected-file evidence link: {s["id"]} / {inspected["path"]}')
    if 'retirement' not in page.searches.get('source-O08', ''):
        errors.append('Suggested retirement query cannot find its primary evidence')
    skills = list((ROOT / 'skills').glob('*/SKILL.md'))
    manifest = json.loads((ROOT / 'skills/manifest.json').read_text())
    if {str(p.relative_to(ROOT)) for p in skills} != {s['path'] for s in manifest['skills']}:
        errors.append('Skill manifest and skill directories differ')
    for skill in skills:
        text = skill.read_text()
        if not text.startswith('---\n') or not re.search(r'^name: [a-z0-9-]+$', text, re.M) or not re.search(r'^description: .+', text, re.M):
            errors.append(f'Invalid skill frontmatter: {skill.relative_to(ROOT)}')
    for md in ROOT.rglob('*.md'):
        if any(part.startswith('.') for part in md.relative_to(ROOT).parts):
            continue
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', md.read_text()):
            p = urlsplit(link)
            if p.scheme or p.netloc or not p.path:
                continue
            target = (md.parent / unquote(p.path)).resolve()
            if not target.exists():
                errors.append(f'Broken Markdown reference in {md.relative_to(ROOT)}: {link}')
    for name in ('lifecycle', 'delegation', 'adaptation'):
        gif = (ROOT / f'assets/{name}.gif').read_bytes()
        png = (ROOT / f'assets/{name}.png').read_bytes()
        if gif[:6] not in (b'GIF87a', b'GIF89a') or not png.startswith(b'\x89PNG\r\n\x1a\n'):
            errors.append(f'Invalid diagram format: {name}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: 6 reference stages, {len(stages)} modules, {len(skills)} skills, {len(sources)} sources; all local links/assets and evidence mappings resolve.')
    print('PASS: no remote automatic assets or inline scripts/handlers. This is a structural check, not browser or accessibility certification.')
    return 0


if __name__ == '__main__':
    sys.exit(check())
