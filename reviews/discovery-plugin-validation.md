# Discovery research and central Codex installation

Reviewed 30 October 2026. This change enhances the existing discovery skill; the bundle still contains twenty skills. The [8 October validation](deep-validation.md) remains evidence for its original candidate, not a behavioral evaluation of this revision.

## Change

Discovery accepts a rough idea, chooses research that can affect product decisions, inspects sources and connects findings to proposed scope. It distinguishes capabilities and vendor claims from demand hypotheses, handles unavailable browsing honestly, and preserves explicit user constraints. Outputs belong to the active product workspace, with a separate research record only when useful.

The root portable plugin manifest and `.agents/plugins/marketplace.json` package the entire repository so shared references remain intact. The native Codex installer registers `ai-sdlc-local` and installs/enables `ai-sdlc@ai-sdlc-local` at user scope. No hooks, MCP servers, automatic publishing or background jobs are added.

## Observed validation

- `python3 -B scripts/build.py`: successful regeneration.
- `python3 -B scripts/check_skills.py`: twenty skills, nineteen inventoried practices, referenced templates and configuration paths resolve.
- `python3 -B scripts/check_site.py`: local links/assets, stage mapping and static site integrity pass.
- `python3 -B -m unittest discover -s tests -v`: all eighteen profile tests pass.
- `node --check assets/app.js` and `node tests/test_controls.cjs`: pass.
- Official skill-creator `quick_validate.py`: updated discovery skill passes. System Python lacked PyYAML; validation succeeded using an existing cached PyYAML module without installation.
- `git diff --check`: pass.
- Codex CLI 0.166.0: marketplace registration and plugin installation succeed; `plugin list` from outside the kit reports version 0.1.0 installed and enabled.
- Installed snapshot: all twenty skill files plus the shared contract, research instructions/templates, manifest and README match the source files checked at installation.
- Native `skills/list` with `forceReload: true`, invoked through `codex app-server` in a fresh temporary Git repository: all twenty expected plugin-qualified skills are enabled, with no reported discovery errors. The entry point is `ai-sdlc:ai-sdlc-discover`, display name **Product idea to intent**, scope **user**. No thread or model task was started. The first probe assumed unqualified names; inspecting the actual response corrected the invocation documentation, and the qualified-name assertion passed.

Native app-server initialization required access to Codex's user state database; the initial sandbox-only attempt could not initialize it. The authorized metadata probe completed using the normal user runtime. Temporary project files were removed after the check.

## Limits

These checks establish packaging, installation, discovery and local structural integrity. They do not demonstrate the revised skill's live research quality, automatic selection, product decision quality or output behavior on a real idea. No new independent behavioral comparison, market-research task or accessibility/browser review ran. The plugin uses tools available in the invoking host; installing it does not supply web access or external service authorization.

The installation is local to this user and machine. Other users need their own installation, and managed or project settings can restrict it. This repository remains the update source; installed files are cached. See [installation and usage](../README.md#install-once-for-codex).
