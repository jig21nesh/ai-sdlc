# AI-SDLC skill pack

This folder contains **20 implemented skills** grounded in [Anthropic's AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), with deeper GitHub and Medium research, reusable output templates and organization/project adaptation points.

Start with the [research synthesis](research/SYNTHESIS.md) and [practice-to-skill coverage](research/practice-coverage.md). Open [index.html](index.html) for the plain HTML index, evidence search and three original GIF explanations. It uses local assets and works without a build; JavaScript adds optional controls.

## Use the skills

1. Choose the relevant procedure from [skills/manifest.json](skills/manifest.json) or the HTML skill library. Initial intent uses `ai-sdlc-discover`; `ai-sdlc-plan` plans implementation within Build.
2. Give your agent the selected `skills/ai-sdlc-…/SKILL.md` path, the actual request, repository and relevant policy references. For example: “Use skills/ai-sdlc-verify/SKILL.md to assess this candidate against these acceptance criteria.”
3. Use the short [task brief](templates/TASK-BRIEF.md) where helpful. A small task does not require completing the full organization profiles.
4. Keep the bundle together so relative references resolve. The procedures read the shared contract and load supporting templates only when useful.
5. For repeated organizational use, configure owned profiles and runtime adapters using [config/ADAPTATION.md](config/ADAPTATION.md). Verify actual controls separately from profile declarations.

The skills are local instruction files, **not globally installed skills or running automation**. Automatic discovery depends on the host and its configured skill directories. Supply explicit paths or package the bundle using the host's documented discovery mechanism; no particular vendor layout is assumed.

## What is implemented

| Phase | Skills |
| --- | --- |
| Plan | discover |
| Design | specify, design |
| Build | plan, build, repository-context, policy-skills, orchestrate |
| Test | verify, agent-evals |
| Deploy | review, release |
| Maintain | operate, security-scanning, improve |
| Cross-cutting | govern, guardrails, security-review, usability-review |
| Supplemental | retire |

Each skill has a specific trigger, substantive procedure, output/evidence contract, failure handling and local adaptation fields. The [19-item source inventory](research/playbook-inventory.json) covers source practices, sidebars and cross-cutting concepts. These are different units from the 20 skills and the 12 navigation modules. Retirement is additional lifecycle coverage, not an Anthropic stage.

## Research and customization

- [Primary analysis](research/deep-primary-analysis.md): phase placement, dependencies, runtime caveats and capability gaps.
- [GitHub analysis](research/deep-github-analysis.md): seven repositories inspected at recorded SHAs, with 47 selected file observations.
- [Medium analysis](research/deep-medium-analysis.md): twelve records; eleven bodies read and one partial article excluded from implementation support.
- [Consolidated evidence](research/evidence.json): 43 unique source URLs, with access/inspection limits and aliases. Repeated URLs count once.
- [Configuration guide](config/ADAPTATION.md): exact organization, project and adapter changes.
- [Agent briefs](agents/roles.md): optional delegation contracts, not installed agents.
- [Current validation](reviews/deep-validation.md): checks, behavioral exercises, findings and remaining limits.

The core method stays stable. Organization files supply policy and accountability; project files supply architecture, commands and acceptance; adapters supply actual permissions, tools, CI, scheduling and external integrations. Example profiles contain unresolved values intentionally. No profile or Markdown instruction grants authority or enforces a sandbox.

## Regenerate and validate

Python 3.10+ and Node.js are used for local checks, not to read the guide.

```sh
python3 scripts/build.py
python3 scripts/check_skills.py
python3 scripts/check_site.py
python3 scripts/validate_profiles.py --org config/org.example.json --project config/project.example.json
python3 -m unittest discover -s tests -v
node --check assets/app.js
node tests/test_controls.cjs
```

To check populated profiles, pass your own files and add `--ready`. Readiness validates declarations, not referenced approval records or live controls. The validator never executes configured commands or loads adapters.

`scripts/build.py` regenerates the HTML, consolidated evidence and module evidence map. Edit its source rather than the generated HTML. The GIFs are already provided; optional regeneration uses `uv run --with pillow==11.3.0 python scripts/generate_gifs.py`.

## Scope of confidence

Research reviewed 8 October 2026. GitHub files and tests were inspected, not executed upstream. Medium accounts are practitioner evidence, not benchmarks or authority. The original procedures/templates do not copy upstream executors. Source licenses remain with their owners; no repository-wide license is chosen on your behalf.

Coverage is traceable to the selected primary reference, not a claim to have exhausted every AI-SDLC practice. Production controls, vendor terms, regulatory requirements and runtime discovery require local validation. Live browser and assistive-technology checks were unavailable here; see the current validation report.
