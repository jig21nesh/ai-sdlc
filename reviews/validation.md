# Implementation validation

Historical review of an earlier revision. See [deep-validation.md](deep-validation.md) for the current 20-skill pack and its evidence.

Historical first-implementation report. For the current six-stage reference, updated skills and expanded evidence register, read [playbook-validation.md](playbook-validation.md). The hashes and counts below identify the earlier candidate.

Date: 2026-10-08. This report covers the local guide, skill bundle and inert configuration validator. It does not validate a production agent runner, organization deployment or external provider.

## Observed checks

| Check | Result and scope |
| --- | --- |
| Profile behavior | 18 Python unit tests passed, including unresolved readiness, policy subset restrictions, legal holds, mutation declarations, literal argv handling, malformed URLs and safe error diagnostics. |
| Example profiles | Structural validation passed using the explicit `--org` and `--project` example paths. Readiness intentionally fails on unresolved decisions. |
| JavaScript syntax | `node --check assets/app.js` passed. |
| Interaction logic | `node tests/test_controls.cjs` passed for GIF play/pause, reduced-motion preference changes, stage expansion, filtering, empty results, hostile search text as literal input, malformed hashes and deep links. These use a minimal DOM fixture, not a browser. |
| Static guide integrity | Passed after all review files were complete: 12 stages, 15 skills and 31 sources; local files/fragments, source mappings, skill frontmatter, Markdown references and diagram signatures resolve. No automatic remote assets or inline script handlers. |
| Diagram assets | Generator checked three GIFs, four distinct frames per GIF, looping, 1080×420 dimensions and 2.4-second frame timing. Both the asset author and integrating agent visually inspected all three static equivalents. |
| Source records | 31 attributed records, explicit access limitations, stage mappings and a generated combined register. Research was read-only; third-party code was not installed or executed. |
| Security review | Independent reviewer reproduced three low-severity validator issues, then confirmed fixes and passing regression checks. Build escaping and unsafe URL rejection were exercised in isolated fixtures. See the security report. |
| Usability review | Independent static review examined first-use documentation, source search, mobile navigation, contrast and motion behavior. Findings were fixed and rechecked. See the usability report. |
| Skill forward-test | The independent security reviewer produced a simulated plan/release handoff for missing policy/candidate evidence and an injection-bearing issue comment. Useful reversible preparation proceeded; fabricated authority and data-exfiltration instructions did not become accepted actions. No live agent runtime was exercised. |
| Regeneration | Rebuilding twice produced identical hashes for HTML, combined evidence and the stage/source mapping. |

Final integration rebuilt the assurance section with the completed reviews and reran the local-link and control checks successfully. The resulting `index.html` SHA-256 is `6bbc054b4f2eeebfbeb7479fddb6953d51596fc5f873dd9c4d05d09ad5f25637`. This later build changes the review-status content from the reviewers' earlier HTML snapshot; the reviewed behavior and configuration fixes are unchanged.

## Browser and environment limits

The available browser automation rejects `file://` URLs. Starting a loopback HTTP preview server was also denied by the filesystem/network sandbox. No browser security policy was changed or bypassed. Live desktop/mobile rendering, keyboard interaction, screen-reader behavior, browser console/network behavior and actual browser reduced-motion rendering therefore remain **unverified**. Responsive CSS and accessibility semantics were inspected, but this is not a WCAG conformance audit.

The official skill-creator `quick_validate.py` initially could not run because the system Python lacked PyYAML. A uv attempt could not use the restricted default cache; a temporary-cache attempt encountered a uv system-configuration failure. Dependency-free checks cover skill frontmatter, names, links and unfinished scaffolding instead; they do not prove behavioral correctness.

The delivered page can be opened directly by the user from `index.html`. Source links require internet access. Before adopting the toolkit in an organization, test the guide in the intended browsers and configure/validate the actual agent host, CI and authorization controls.

## Reproduce local checks

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests -v
python3 scripts/validate_profiles.py --org config/org.example.json --project config/project.example.json
node --check assets/app.js
node tests/test_controls.cjs
python3 scripts/check_site.py
```

To verify the deliberate unresolved state, add `--ready` to the example-profile command and expect exit code 1 with field-specific decisions. Do not replace unknown decisions with arbitrary text merely to make the check pass.
