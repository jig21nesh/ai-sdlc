# AI-SDLC skill pack

This folder contains **20 implemented skills** grounded in [Anthropic's AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), with deeper GitHub and Medium research, reusable output templates and organization/project adaptation points.

Start with the [research synthesis](research/SYNTHESIS.md) and [practice-to-skill coverage](research/practice-coverage.md). Open [index.html](index.html) for the plain HTML index, evidence search and three original GIF explanations. It uses local assets and works without a build; JavaScript adds optional controls.

## Start with a rough product idea

Open the **product's folder** in Codex and invoke the installed discovery skill:

```text
Use $ai-sdlc:ai-sdlc-discover.

My idea: <describe the product or problem in your own words>.
Explore the idea, research relevant competitors, alternatives and feasibility,
and draft the intent in this project. Ask focused questions where needed.
```

A short description is enough. The skill selects research that can change the product decision, inspects available sources, and separates evidence from assumptions. It does not require a competitor report for an internal bug fix. You can specify a region, audience, time limit or offline-only scope. Browsing requires the host's available tools and permissions; missing access is reported, never replaced with invented market claims.

Outputs follow the product's existing convention. Otherwise discovery writes `docs/intent.md` and, for substantial research, `docs/research.md`. A distinct idea gets its own directory under `docs/intents/` if the default intent already belongs to other work. The installed kit remains separate from product output. Existing files are inspected and preserved or updated within the actual task.

Review the draft, then ask for `ai-sdlc-specify` to produce the specification, followed by `ai-sdlc-plan` and `ai-sdlc-build` when ready. A discovery request ends with the intent and next decision; it does not start implementation automatically.

## Install once for Codex

Install the whole repository as a **user-scoped plugin** so its twenty skills and shared relative references stay together. The root [plugin.json](plugin.json) is the package manifest; the repository's `.agents/plugins/marketplace.json` exposes it through the `ai-sdlc-local` marketplace. No model service, connector, hook or background job is bundled.

From this kit's root, with a Codex CLI that supports `plugin add`:

```sh
codex plugin marketplace add "$PWD"
codex plugin add ai-sdlc@ai-sdlc-local
codex plugin list --marketplace ai-sdlc-local --json
```

Then open a new Codex chat in any product repository and select **Product idea to intent**, or invoke `$ai-sdlc:ai-sdlc-discover`. Codex 0.166.0 exposes installed skills as `ai-sdlc:<skill-name>`; the source skill's name remains `ai-sdlc-discover`. In the desktop app, restart if the installed plugin has not appeared. Clients without `plugin add` can register the marketplace and install **AI SDLC** through the desktop Plugins directory.

The native plugin installer manages the user configuration and cache; product repositories need no copies of the kit. Keep this checkout available as the local update source. Installed files are a cached snapshot: after updating this checkout, rerun `codex plugin add ai-sdlc@ai-sdlc-local`, verify the installed version, and start a new chat. A team can distribute an accepted revision through a Git-backed marketplace later. This local installation does not publish the package or make it available automatically on another machine.

The commands are supported by the locally inspected Codex CLI 0.166.0. [Official plugin packaging documentation](https://developers.openai.com/plugins/build/plugins) describes package structure, marketplace scope and cached installations; check the installed client's help when adopting another version. A project or administrator can disable a plugin even when it is installed for the user.

## Use the skills

1. Choose the relevant procedure from [skills/manifest.json](skills/manifest.json) or the HTML skill library. Initial intent uses `ai-sdlc-discover`; `ai-sdlc-plan` plans implementation within Build.
2. Give your agent the selected `skills/ai-sdlc-…/SKILL.md` path, the actual request, repository and relevant policy references. For example: “Use skills/ai-sdlc-verify/SKILL.md to assess this candidate against these acceptance criteria.”
3. Use the short [task brief](templates/TASK-BRIEF.md) where helpful. A small task does not require completing the full organization profiles.
4. Keep the bundle together so relative references resolve. The procedures read the shared contract and load supporting templates only when useful.
5. For repeated organizational use, configure owned profiles and runtime adapters using [config/ADAPTATION.md](config/ADAPTATION.md). Verify actual controls separately from profile declarations.

Cloning this repo alone does not install its skills. Use the plugin setup above for central Codex discovery, or supply explicit `skills/ai-sdlc-…/SKILL.md` paths with any capable agent. For example, point the agent at the discovery file's absolute path while working in the product repo. Keep the bundle intact. Other hosts need their own supported packaging; the procedures themselves remain portable.

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
- [Discovery and plugin validation](reviews/discovery-plugin-validation.md): current discovery changes, central installation and native host discovery checks.
- [Original pack validation](reviews/deep-validation.md): earlier behavioral exercises, findings and their limits.

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
