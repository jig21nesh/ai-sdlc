#!/usr/bin/env python3
"""Render a buildless, offline-readable guide from local evidence and stage records."""
import html
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def esc(value):
    return html.escape(str(value), quote=True)


def items(values):
    return '<ul>' + ''.join(f'<li>{esc(v)}</li>' for v in values) + '</ul>'


def https_url(value):
    parsed = urlsplit(value)
    if parsed.scheme != 'https' or not parsed.netloc or parsed.username or parsed.password:
        raise ValueError(f'Invalid evidence URL: {value!r}')
    return esc(value)


def read(name):
    return json.loads((ROOT / name).read_text())


def source_catalog():
    """Preserve stable IDs while enriching repeated URLs with deeper inspection."""
    records = {}
    for kind in ('official', 'github', 'medium', 'deep-github', 'deep-medium'):
        for record in read(f'research/{kind}-sources.json'):
            key = record['url'].rstrip('/')
            previous = records.get(key)
            if previous:
                record = {**previous, **record, 'id': previous['id'],
                          'aliases': sorted(set(previous.get('aliases', []) + [record['id']]))}
            records[key] = record
    return list(records.values())


def build():
    stages = read('data/stages.json')
    reference = read('data/reference-model.json')
    animations = read('assets/animations.json')
    sources = source_catalog()
    manifest = read('skills/manifest.json')
    skills = manifest['skills']
    if len({s['id'] for s in sources}) != len(sources):
        raise ValueError('Duplicate evidence IDs')
    source_index = {key: s for s in sources for key in [s['id'], *s.get('aliases', [])]}
    source_counts = {kind: sum(s['type'] == kind for s in sources) for kind in ('primary', 'repository', 'practitioner')}
    mapping = {
        'govern': ['O01','O02','O07','O08','O09','G10','M04'],
        'discover': ['O02','O04','O08','G01','M02'],
        'specify': ['O02','O06','O07','G01','M03'],
        'design': ['O03','O04','O07','O09','G03','G04','M01'],
        'plan': ['O03','O04','O07','G01','G10','M02'],
        'build': ['O05','O07','O09','G02','G06','M03'],
        'verify': ['O06','O07','O09','G03','G05','M05'],
        'review': ['O06','O09','O13','G06','M04'],
        'release': ['O07','O10','O11','G07','M04'],
        'operate': ['O08','O09','O12','G08','M06'],
        'improve': ['O01','O02','O06','O14','G05','M05'],
        'retire': ['O08']
    }
    for module in stages:
        if module['id'] != 'retire':
            mapping[module['id']].insert(0, 'O15')
    mapping['build'] += ['O16', 'O17']
    mapping['plan'] += ['O17', 'O18']
    mapping['release'] += ['O16', 'O18']
    (ROOT / 'data/evidence-map.json').write_text(json.dumps(mapping, indent=2) + '\n')

    def refs(ids):
        return ''.join(f'<a class="ref" href="#source-{esc(source_index[i]["id"])}" title="{esc(source_index[i]["title"])}">{esc(i)}</a>' for i in ids)

    stage_cards = []
    for stage in stages:
        skill_path = f'skills/ai-sdlc-{stage["id"]}/SKILL.md'
        stage_cards.append(f'''
<details class="stage" id="stage-{esc(stage['id'])}">
  <summary><span class="step-number">M{esc(stage['number'])}</span><span class="stage-heading"><strong>{esc(stage['name'])}</strong><span>{esc(stage['question'])}</span></span><span class="plus" aria-hidden="true">+</span></summary>
  <div class="stage-body">
    <p class="placement"><strong>Reference placement:</strong> {esc(stage['placement'])}. This work module is our synthesis.</p>
    <p class="stage-intro">{esc(stage['summary'])}</p>
    <div class="pills">{''.join(f'<span>{esc(v)}</span>' for v in stage['skills'])}</div>
    <h4>What happens here</h4>{items(stage['activities'])}
    <div class="split"><div><h4>Inputs</h4>{items(stage['inputs'])}</div><div><h4>Evidence to leave behind</h4>{items(stage['outputs'])}</div></div>
    <div class="gate"><h4>Completion evidence & applicable acceptance</h4><p>{esc(stage['gate'])}</p><p><strong>Accountable people:</strong> {esc(stage['human'])}</p></div>
    <div class="split"><div><h4>Where to adapt</h4><p class="code-list">{''.join(f'<code>{esc(v)}</code> ' for v in stage['configure'])}</p></div><div><h4>Useful measures</h4>{items(stage['metrics'])}</div></div>
    <p class="watch"><strong>Watch for:</strong> {esc(stage['failure'])}</p>
    <div class="stage-footer"><a class="text-link" href="{skill_path}">Read {esc('ai-sdlc-' + stage['id'])} skill</a><div class="references" aria-label="Supporting sources">{refs(mapping[stage['id']])}</div></div>
  </div>
</details>''')

    evidence_cards = []
    kinds = {'primary':'Primary guidance', 'repository':'GitHub repository', 'practitioner':'Medium perspective'}
    for s in sources:
        stage_names = [stage['name'] for stage in stages if stage['id'] in s['stages']]
        aliases = ['retirement decommissioning'] if 'retire' in s['stages'] else []
        search = ' '.join([s['id'],*s.get('aliases', []),s['title'],s['publisher'],s['summary'],s['limitations'],*s['supports'],*s['stages'],*stage_names,*aliases]).lower()
        inspection = ''
        if s.get('inspected_files'):
            inspection = '<h4>Pinned files inspected</h4><ul>' + ''.join('<li><a href="' + https_url(f['url']) + '">' + esc(f['path']) + '</a>: ' + esc(f['observation']) + '</li>' for f in s['inspected_files']) + '</ul>'
        if s.get('aliases'):
            inspection += '<p>Deep-research IDs: ' + esc(', '.join(s['aliases'])) + '. Repeated URLs count once.</p>'
        evidence_cards.append(f'''
<article class="source-card" id="source-{esc(s['id'])}" data-kind="{esc(s['type'])}" data-search="{esc(search)}">
  <div class="source-meta"><span class="source-id">{esc(s['id'])}</span><span>{kinds[s['type']]}</span><span class="access {esc(s['access'])}">{'Full page read' if s['access']=='full' else 'Partial access' if s['access']=='partial' else 'Search only'}</span></div>
  <h3><a href="{https_url(s['url'])}" rel="noreferrer">{esc(s['title'])}</a></h3>
  <p class="byline">{esc(s['publisher'])} · {esc(s['published'] or 'Publication date not verified')}</p>
  <p>{esc(s['summary'])}</p>
  <details><summary>Evidence & limitations</summary><div class="source-detail"><h4>What it supports</h4>{items(s['supports'])}<h4>Limits of this evidence</h4><p>{esc(s['limitations'])}</p>{'<p><strong>License:</strong> ' + esc(s['license']) + '</p>' if s.get('license') else ''}<p><strong>Relevant work modules:</strong> {esc(', '.join(s['stages']))}</p>{inspection}<p>Reviewed {esc(s['accessed'])}. “Full page read” means the linked page was accessible; it does not mean every linked document or repository file was audited.</p></div></details>
</article>''')

    skill_rows = ''.join(f'<tr><th scope="row">{esc(s["phase"])} · {esc(s["purpose"])}</th><td>{refs(s["evidence_ids"])}</td><td><a href="{esc(s["path"])}">{esc(s["id"])}</a></td></tr>' for s in skills)
    stage_nav = ''.join(f'<a href="#stage-{esc(s["id"])}"><span>M{esc(s["number"])}</span>{esc(s["name"])}</a>' for s in stages)
    modules_by_id = {s['id']:s for s in stages}
    phase_cards = ''.join('<article class="phase-card"><span class="mini-label">REFERENCE STAGE ' + str(i+1) + '</span><h3>' + esc(phase['name']) + '</h3><ul>' + ''.join('<li><a href="#stage-' + esc(m) + '">' + esc(modules_by_id[m]['name']) + '</a></li>' for m in phase['modules']) + '</ul></article>' for i,phase in enumerate(reference['stages']))
    coverage_rows = ''.join(f'<tr><th scope="row">{esc(s["name"])}</th><td>{refs(mapping[s["id"]])}</td><td>{"Primary guidance only; no strong repository or Medium evidence in this sample." if s["id"]=="retire" else "Our synthesis; sources support patterns, not this exact stage contract."}</td></tr>' for s in stages)
    review_path = ROOT / 'reviews/results.json'
    review = json.loads(review_path.read_text()) if review_path.exists() else {'status':'Implementation in progress', 'summary':'Independent security and usability reviews will run after implementation.', 'checks':[]}
    review_checks = items(review['checks'])

    def figure(name):
        meta = animations[name]
        return f'<figure><img src="assets/{name}.png" data-gif="assets/{name}.gif" data-still="assets/{name}.png" width="1080" height="420" alt="{esc(meta["alt"])}" loading="lazy"><figcaption>{esc(meta["caption"])} <a href="assets/{name}.png">Full-size diagram</a> · <a href="assets/{name}.gif">Open GIF</a></figcaption></figure>'

    content = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="no-referrer">
<meta name="description" content="Anthropic's six-stage AI-native SDLC reference mapped to 12 reusable work modules, {len(skills)} portable skills, source evidence and organization configuration.">
<title>AI SDLC Field Guide — from intent to evidence</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/styles.css">
<script src="assets/app.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<aside class="sidebar">
  <a class="brand" href="#overview"><span class="brand-mark" aria-hidden="true">a/</span><span>AI SDLC<span class="brand-sub">FIELD GUIDE</span></span></a>
  <p class="nav-label">THE PLAYBOOK</p>
  <nav aria-label="Main navigation"><a href="#overview">Overview</a><a href="#reference">Reference stages <span>6</span></a><a href="#lifecycle">Work modules <span>12</span></a><a href="#skills">Skill library <span>{len(skills)}</span></a><a href="#adapt">Adapt to your organization</a><a href="#agents">Agent collaboration</a><a href="#evidence">Evidence library <span>{len(sources)}</span></a><a href="#assurance">Security & usability review</a></nav>
  <div class="sidebar-bottom"><span class="edition">RESEARCH SNAPSHOT</span><p>08 October 2026</p><p>Plain HTML. Local assets.<br>No account or build required.</p><a href="README.md">Repository guide</a></div>
</aside>
<main id="main">
<header class="topbar"><span>ENGINEERING PRACTICE / 01</span><a href="research/evidence.json" download>Download evidence JSON</a></header>
<section class="hero" id="overview">
  <div class="eyebrow"><span></span> A practical, evidence-backed blueprint</div>
  <h1>AI across the <em>whole</em><br>software lifecycle.</h1>
  <p class="lead">Twenty reusable skills for the whole delivery loop, grounded in Anthropic’s playbook and detailed GitHub and Medium research. Choose a procedure, supply local context, and retain evidence of the result.</p>
  <div class="hero-actions"><a class="button primary" href="README.md#start-with-a-rough-product-idea">Start with an idea</a><a class="button" href="#skills">Choose a skill</a><a class="button" href="README.md#install-once-for-your-host">Install for Codex or Claude Code</a></div>
  <div class="stats"><div><strong>6</strong><span>reference stages</span></div><div><strong>{len(skills)}</strong><span>portable skills</span></div><div><strong>{len(sources)}</strong><span>linked sources</span></div><div><strong>3</strong><span>animated explanations</span></div></div>
  <div class="scope-note"><strong>Scope:</strong> AI assisting software delivery, including evaluation of the delivery agent itself. Product AI adds a separate evaluation scope. Anthropic supplies the six-stage reference; our 12 work modules, configuration and controls are a broader synthesis. This is a guide, not an autonomous deployment system or compliance certification.</div>
</section>
<section class="section" id="reference" aria-labelledby="principles-title">
  <div class="section-top"><div><p class="eyebrow">THE REFERENCE MODEL</p><h2 id="principles-title">Six stages. Twelve detailed work modules.</h2></div><button id="motion-toggle" class="button" type="button" aria-pressed="false" hidden>Play animations</button></div>
  <p class="section-lead">The stage names below follow <a href="https://claude.com/resources/articles/the-ai-native-sdlc-playbook" rel="noreferrer">Anthropic’s AI-native SDLC playbook</a>. Each box links to our corresponding work modules. This mapping is our interpretation, with stable skill names for reuse.</p>
  {figure('lifecycle')}
  <div class="phase-grid">{phase_cards}</div>
  <div class="callout"><strong>Read the boxes at the right level</strong><p>Initial intent belongs to Plan; implementation planning is a Build activity. <a href="#stage-govern">Governance</a> runs across the loop. <a href="#stage-retire">Retirement</a> is additional coverage from this toolkit. The article’s adoption graph is a separate view, not an execution sequence. {refs(['O15'])}</p><p><a href="research/playbook-reconciliation.md">Read the source reconciliation and corrections</a></p></div>
  <p class="small" id="motion-note">Diagrams start still. Play the GIFs when useful; each has a static equivalent and a text explanation.</p>
  <div class="principles"><article><span class="mini-label">01 / ORGANIZATION</span><h3>Improve the delivery system</h3><p>Policy clarity, reliable context, small changes and user feedback matter alongside model capability.</p><p class="references">{refs(['O01','O02'])}</p></article><article><span class="mini-label">02 / ORCHESTRATION</span><h3>Start with a bounded workflow</h3><p>Use a defined sequence for predictable tasks. Add autonomous decisions or more agents when the task and measured results justify them.</p><p class="references">{refs(['O03'])}</p></article><article><span class="mini-label">03 / ASSURANCE</span><h3>Verify the resulting state</h3><p>Inspect artifacts, tests and outcomes. A persuasive completion message is not evidence of success or permission to act.</p><p class="references">{refs(['O06','O09'])}</p></article></div>
</section>
<section class="section" id="lifecycle">
  <div class="section-top"><div><p class="eyebrow">01 / WORK MODULES</p><h2>Choose the work this change needs.</h2></div><button id="expand-stages" class="button" type="button" aria-expanded="false" aria-controls="stage-list" hidden>Expand all modules</button></div>
  <p class="section-lead">M00–M11 are module IDs, not twelve vendor stages or mandatory sequential approvals. Open a module for activities, inputs, evidence and accountable owners. Requirements and design can share a working session; checks continue during implementation. Apply review requirements according to risk and existing policy.</p>
  <div class="stage-jumps" aria-label="Jump to a work module">{stage_nav}</div>
  <div id="stage-list">{''.join(stage_cards)}</div>
  <details class="coverage"><summary>See the module-to-evidence map and coverage gaps</summary><div class="table-scroll" role="region" aria-label="Module evidence mapping" tabindex="0"><table><thead><tr><th>Work module</th><th>Evidence</th><th>Interpretation</th></tr></thead><tbody>{coverage_rows}</tbody></table></div></details>
</section>
<section class="section" id="skills">
  <p class="eyebrow">02 / SKILL LIBRARY</p><h2>Portable procedures. Specific triggers.</h2>
  <p class="section-lead">The 20 skills implement 19 inventoried playbook practices and supporting lifecycle work. Each contains a decision procedure, concrete output contract, failure handling, adaptation points and sources. <a href="research/SYNTHESIS.md">Read the research-to-implementation analysis</a> or <a href="skills/manifest.json">machine-readable skill map</a>. Keep the bundle together so shared references resolve. SKILL.md files are usable agent instructions with optional output templates; no host runtime or automatic discovery has been installed.</p>
  <div class="callout"><strong>Use a skill in your agent</strong><p>Provide the selected skill path, your request and the relevant repository or artifacts. For example:</p><pre><code>Use skills/ai-sdlc-plan/SKILL.md to plan this change.
Read the attached specification and repository.</code></pre><p><a href="README.md#use-the-skills">Read the usage instructions</a>. For a small task, the <a href="templates/TASK-BRIEF.md">short task brief</a> is sufficient when it supplies the relevant context.</p></div>
  <div class="table-scroll" role="region" aria-label="Skills by phase" tabindex="0"><table><thead><tr><th>Phase / practice</th><th>Evidence</th><th>Skill file</th></tr></thead><tbody>{skill_rows}</tbody></table></div>
  <div class="skill-extras"><a href="skills/ai-sdlc-orchestrate/SKILL.md"><span>Cross-cutting</span><strong>Orchestrate bounded work</strong><p>Route tasks, isolate edits and integrate evidence.</p></a><a href="skills/ai-sdlc-security-review/SKILL.md"><span>Cross-cutting</span><strong>Review security</strong><p>Inspect trust boundaries, tool access and failure cases.</p></a><a href="skills/ai-sdlc-usability-review/SKILL.md"><span>Cross-cutting</span><strong>Review usability</strong><p>Test real journeys, accessibility and recovery.</p></a></div>
  <div class="callout"><strong>Adoption path</strong><p>Choose one bounded task. Use the <a href="templates/TASK-BRIEF.md">task brief</a> and only the relevant skills. Supply applicable policy and project facts, then compare actual results with the baseline. Expand only after reviewing evidence. <a href="skills/shared-contract.md">Read the shared skill contract</a>.</p></div>
</section>
<section class="section" id="adapt">
  <p class="eyebrow">03 / ORGANIZATION ADAPTATION</p><h2>Change the settings, not every skill.</h2>
  <p class="section-lead">Keep reusable methods stable. Version your policy decisions, project facts and integration settings separately. A project configuration must not weaken organization policy.</p>
  {figure('adaptation')}
  <div class="table-scroll" role="region" aria-label="Organization customization points" tabindex="0"><table><thead><tr><th>Layer / file</th><th>What to change</th><th>Who owns it</th></tr></thead><tbody>
  <tr><th scope="row"><a href="skills/shared-contract.md">Core skills & shared contract</a></th><td>Improve the reusable procedure only when a demonstrated failure or missing capability warrants it. Retain evidence contracts and scope boundaries.</td><td>Engineering enablement</td></tr>
  <tr><th scope="row"><a href="config/org.example.json">config/org.example.json</a></th><td>Accountable roles, allowed data/models/tools, retention and residency, risk gates, release controls, incident and audit requirements.</td><td>Engineering, security, privacy & service owners</td></tr>
  <tr><th scope="row"><a href="config/project.example.json">config/project.example.json</a></th><td>Product outcomes, architecture, risk tier, trusted context, test commands, artifact paths, service objectives, rollout, rollback and retirement plan.</td><td>Product & technical owners</td></tr>
  <tr><th scope="row"><a href="config/ADAPTATION.md">Runtime adapters</a></th><td>Map your model provider, source control, issue tracker, CI/CD, artifact store and telemetry backend to scoped operations. Enforce authorization in these systems.</td><td>Platform & operations owners</td></tr>
  </tbody></table></div>
  <div class="split onboarding"><div><h3>Use it in a new organization</h3><ol><li>Copy the example profiles and keep policy decisions separate from project facts.</li><li>Resolve required fields with the named owners. Use references to secrets, never secret values.</li><li>Map commands and adapters to the actual repository and sandbox. Review them before any execution.</li><li>Validate structure, then readiness. Unresolved templates intentionally fail readiness.</li><li>Pilot a bounded change, independently review its evidence, and improve from measured results.</li></ol></div><div><h3>Validate your profiles</h3><pre><code>python3 scripts/validate_profiles.py \\
  --org config/org.example.json \\
  --project config/project.example.json

# After editing your own profile copies:
python3 scripts/validate_profiles.py \\
  --org config/org.local.json \\
  --project config/project.local.json \\
  --ready</code></pre><p class="small">The validator inspects configuration. It never executes configured commands, deploys, contacts providers or grants permissions. A passing readiness check cannot certify your runtime controls.</p><a class="text-link" href="config/ADAPTATION.md">Read the full adaptation and integration guide</a></div></div>
  <details class="coverage"><summary>How much process does a change need?</summary><div class="source-detail"><p><strong>Low-impact edit:</strong> use the relevant specification, implementation and review steps with a small evidence note. Existing task authorization covers ordinary reversible work.</p><p><strong>Service or dependency change:</strong> add interface, security, integration, observability and rollback checks proportional to the affected system.</p><p><strong>Sensitive data, production or destructive change:</strong> resolve the applicable organization policy and exact action authority, involve the required owners, and enforce controls in the runtime. Reuse valid existing authorization; do not ask again without a changed scope or requirement.</p><p>Record why a stage or check is not applicable. Unknown high-risk requirements are not automatic exemptions.</p></div></details>
</section>
<section class="section" id="agents">
  <p class="eyebrow">04 / AGENT COLLABORATION</p><h2>Delegate work. Keep accountability.</h2>
  <p class="section-lead">Parallel work is useful for independent research and specialist review. A coordinator owns integration; workers receive only the context and tools needed for their task.</p>
  {figure('delegation')}
  <div class="principles"><article><h3>Make the handoff concrete</h3><p>State the objective, input artifacts, allowed paths and tools, expected evidence, dependencies, budget and stop condition.</p><a href="references/task-brief.example.json">Task brief template</a></article><article><h3>Separate production from review</h3><p>Inspect actual artifacts and outcomes. Give reviewers a fresh task and avoid telling them which verdict to reach.</p><a href="references/agent-roles.md">Role definitions</a></article><article><h3>Constrain the execution</h3><p>Use isolated edits, scoped credentials, bounded retries and an escalation owner. Child agents cannot expand the parent's authority.</p><a href="skills/ai-sdlc-orchestrate/SKILL.md">Orchestration skill</a></article></div>
  <p class="small">These are vendor-neutral role briefs. Agent spawning, workspaces, model selection and tool permissions must be configured in the chosen host; no agent runtime is bundled. {refs(['O03','O04','O09','G03','G04'])}</p>
</section>
<section class="section" id="evidence">
  <p class="eyebrow">05 / EVIDENCE LIBRARY</p><h2>Follow the source. Read its limits.</h2>
  <p class="section-lead">{source_counts['primary']} primary guidance sources, {source_counts['repository']} GitHub repositories and {source_counts['practitioner']} Medium articles. Each record separates an observed claim from the limits of what was inspected.</p>
  <div class="evidence-context"><p><strong>Primary guidance</strong> grounds the practices. <strong>GitHub</strong> provides implementation patterns, not an endorsement of every dependency. <strong>Medium</strong> adds practitioner perspectives; technical recommendations are cross-checked against primary material.</p><p>This is a selected research snapshot, not an exhaustive search or proof of completeness. Seven repositories have additional file-level inspection at observed commit SHAs. Other repository records retain their original limited scope; living documentation can change. Repeated source URLs count once. One Medium article is member-only; only its visible introduction is summarized. No third-party code was executed.</p><a href="research/METHODOLOGY.md">Research method & refresh procedure</a></div>
  <div class="evidence-tools" id="evidence-tools" hidden><div><label for="source-query">Search evidence</label><input id="source-query" type="search" placeholder="Try: evaluation, privacy, retirement" autocomplete="off"></div><div><label for="source-kind">Source type</label><select id="source-kind"><option value="all">All sources</option><option value="primary">Primary guidance</option><option value="repository">GitHub repositories</option><option value="practitioner">Medium perspectives</option></select></div><p id="source-count" role="status" aria-live="polite">{len(sources)} sources</p></div>
  <p id="source-empty" class="callout" hidden>No sources match. Try a broader term or select “All sources”.</p>
  <div class="source-grid">{''.join(evidence_cards)}</div>
  <div class="download-row"><a href="research/evidence.json" download>All evidence (JSON)</a><a href="research/deep-primary-analysis.md">Primary-source analysis</a><a href="research/deep-github-analysis.md">GitHub file-level analysis</a><a href="research/deep-medium-analysis.md">Medium analysis</a><a href="research/playbook-inventory.json">Practice inventory</a></div>
</section>
<section class="section" id="assurance">
  <p class="eyebrow">06 / SECURITY & USABILITY</p><h2>Review the kit itself.</h2>
  <p class="section-lead">{esc(review['summary'])}</p>
  <div class="review-status"><span class="mini-label">IMPLEMENTATION REVIEW</span><h3>{esc(review['status'])}</h3>{review_checks}</div>
  <div class="split"><div><h3>Security review scope</h3><p>Prompt injection in source material, privilege escalation across agents, secrets and data exposure, configuration ambiguity, unsafe command execution, source integrity and the browser's external connections.</p><a href="reviews/deep-security-review.md">Read security findings</a></div><div><h3>Usability review scope</h3><p>First-use guidance, discoverability, mobile layout, keyboard navigation, focus, readable source limitations, reduced motion and the difference between a template and an enforced runtime control.</p><a href="reviews/deep-usability-review.md">Read usability findings</a></div></div>
  <p class="small">The <a href="reviews/dual-host-validation.md">dual-host validation</a> records Codex and Claude Code installation checks. The <a href="reviews/discovery-plugin-validation.md">discovery validation</a> records earlier intake changes. The <a href="reviews/deep-validation.md">original skill-pack validation</a> preserves earlier behavioral findings. No review certifies a future organization, provider or deployment; live browser checks remain unverified.</p>
</section>
<footer><a class="brand-footer" href="#overview">AI SDLC / FIELD GUIDE</a><p>© 2026 <a href="https://github.com/jig21nesh">Jignesh Kakkad</a> · <a href="LICENSE">MIT License</a> · Research reviewed 08 October 2026<br>Referenced sources retain their respective owners' licenses and terms.</p><a href="https://github.com/jig21nesh/ai-sdlc">GitHub repository</a><a href="README.md">Open repository guide</a></footer>
</main>
</body>
</html>'''
    (ROOT / 'index.html').write_text(content)
    (ROOT / 'research/evidence.json').write_text(json.dumps(sources, indent=2, ensure_ascii=False) + '\n')
    print(f'Built index.html: 6 reference stages, {len(stages)} work modules, {len(sources)} sources')


if __name__ == '__main__':
    build()
