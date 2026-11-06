# Codex and Claude Code package validation

Reviewed 6 November 2026. Candidate: shared package version **0.2.0**, based on repository commit `28c50ef`, with the packaging and reference moves recorded alongside this report. The base commit ID was updated after ownership metadata and absolute checkout paths were normalized throughout repository history; these remain the original 0.2.0 observations. This is installation and discovery evidence, not an evaluation of product-delivery decisions.

## Changes

- Retained the portable root `plugin.json` and Codex marketplace, and added `.claude-plugin/plugin.json` plus `.claude-plugin/marketplace.json` for Claude Code. Both hosts resolve the same root `skills/` and shared resources.
- Bumped both plugin manifests to 0.2.0. The integrity checker detects mismatched names, versions, descriptions or marketplace roots.
- Moved role documentation and the example handoff into `references/`. Claude previously treated `agents/roles.md` as an agent definition and reported missing frontmatter. The installed package now reports zero agents. Historical review digests retain their original candidate paths.
- Added host-specific installation, invocation and update instructions. Product artifacts still belong to the active product workspace.

## Observed checks

| Check | Observed result |
| --- | --- |
| `python3 -B scripts/build.py` | HTML regenerated with the shared installation entry point and moved reference links. |
| `python3 -B scripts/check_skills.py` | Twenty skills, nineteen inventoried practices, valid references and matching host package metadata. |
| `python3 -B scripts/check_site.py` | Local Markdown/HTML links, assets and evidence mappings resolve. |
| `git diff --check` | No whitespace errors. |
| Claude Code 2.1.318: strict validation of each `.claude-plugin` manifest | Both pass with no manifest errors or warnings. Public-directory submission is outside this check. |
| Claude Code: native marketplace registration and installation | `ai-sdlc@ai-sdlc-local` installed and enabled at user scope, version 0.2.0. |
| Claude Code: `plugin details` from `/private/tmp` | All twenty expected skill names; zero agents, hooks, MCP servers and LSP servers. |
| Codex CLI 0.166.0: native plugin installation | Installed version 0.2.0 through the existing user-scoped marketplace. |
| Codex: app-server `skills/list` with `forceReload: true` in a fresh temporary Git repository | Exactly twenty expected `ai-sdlc:<skill-name>` entries, all enabled, user scope, paths under 0.2.0; no discovery errors. |
| Installed file comparison | Both host caches match the source skill files, shared resources and README. No root agent definitions are present. |

The Codex probe initialized the host and queried metadata only; it started no thread or model turn. The temporary product repository was removed afterward. Claude's local installation reports both a cache and `readFromFolder` pointing at this checkout; keep the checkout available rather than assuming all hosts exclusively read snapshots.

## Limits and supporting documentation

These checks establish packaging, native installation, inventory and reference integrity. They do not establish automatic skill selection, end-to-end research quality, production readiness or equal model behavior. No behavioral agent evaluation, live product task, deployment, browser study or public plugin-directory submission was performed. Claude web and Cowork installation are not included.

Package layout follows [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins) and Claude Code's [manifest reference](https://code.claude.com/docs/en/plugins-reference) and [marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces). Commands were checked against the installed client versions above. User, project or administrator settings can still restrict availability.
