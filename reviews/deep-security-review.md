# Security review of the expanded skill bundle

Reviewed 8 October 2026 using `ai-sdlc-security-review`. Result: **no unresolved security defect demonstrated in the inspected local candidate**. One low-severity source-traceability defect was found and independently rechecked after the integration owner fixed it. This is a limited source review and local-probe result, not proof of runtime enforcement, release authorization or security certification.

## Scope, identity and independence

Scope: all 20 main skill procedures; shared contract; organization/project/adapter declarations and adaptation guidance; agent role/task briefs; shared evidence/task/change templates; selected skill assets, especially guardrails, policy, scanning, release, retirement and evaluation records; Python validator/build/integrity/diagram scripts; browser JavaScript/CSS; and source-catalog consolidation into the generated page. Review traced actionable instructions and data through their actual local consumers. No historical review report or hidden case expectations were read. The existing broad static test results were not assumed to establish semantic correctness.

Reviewer `/root/usability_audit` authored the evaluation, orchestration, general review and usability-review skills and the deep GitHub research. Review of those parts is self-review, not independent assessment. The other 16 skill procedures, including security-review, guardrails, policy-skills and security-scanning, were authored by other agents. This is therefore a **partial cross-author review**, with shared task context. The reviewer did not implement the renderer fix. No independent human security acceptance is claimed.

`git status --short && git rev-parse HEAD` failed with exit 128 because this workspace was not a Git repository. Candidate identity therefore uses file hashes, not an invented commit. At the final inspection, a sorted manifest of 62 selected files had SHA-256 `da0a753778e7a9b1eefcab80f1bb0af75e7922f0b86a731f8d71f0442060aea5`. Construction: select `.md`, `.json`, `.py` files recursively in `skills/`, `config/`, `agents/`, `templates/`, `scripts/`, excluding `__pycache__`; add `README.md`, `index.html`, `assets/app.js`, `assets/styles.css`, `assets/animations.json`; sort workspace-relative paths; concatenate `path + " " + file_sha256 + "\n"`; hash the UTF-8 manifest. Later documentation rebuilds may change the aggregate without changing the reviewed controls.

| Material file | SHA-256 at final inspection |
| --- | --- |
| `scripts/validate_profiles.py` | `73fcb2e54a9d48114efd69dda939c1cbef3c4c0e177f913adaf27fffd5cb0d28` |
| `scripts/build.py` | `f4519f10d0df80c087a6abb1c0db6c60417969a2ca12cf71963c254d8db6f331` |
| `scripts/check_site.py` | `bdef1331f5d5c80bcdb31b79f2f60101c826a59a7db611f0c70f5947d98b7178` |
| `skills/shared-contract.md` | `05acac39cc690f0ccd067c637b7f0fde1cbc8fc5426676aae9b6429fb255ec08` |
| `skills/ai-sdlc-policy-skills/SKILL.md` | `71eee139bd1953dc8580a24e4d13a980f32f06870b1d27216e9eb0117a97a2a6` |
| `index.html` | `a61c2cb693849705411f8549cf2859dfa76278b7e1f8d8ce94536d5f7774b856` |

## Trust boundaries assessed

| Boundary | Observed implementation and limit |
| --- | --- |
| Retrieved policy, issue, log, report or child message → agent action | Shared contract and task-specific procedures preserve source attribution, reject embedded authority changes, keep sensitive data out of handoffs and separate preparation from execution. These instructions are behavioral guidance; no prompt-injection-resistant runtime is installed. |
| Profile JSON → commands, paths, origins and authority | Validator rejects unsupported shape/types, duplicate fields, malformed/oversized input and selected inconsistent scope declarations. It never executes declared commands or loads adapters. Paths are lexical checks; actual filesystem and credential enforcement remain runtime responsibilities. |
| Approval evidence → deployment, operations or deletion | Guardrails/release/operate/retire procedures require actual scope and target/candidate binding, distinguish uncertain completion from failure and preserve state inspection before retries. No trusted approval service, provider adapter or live deny path is supplied. |
| Delegation → shared resources and acceptance | Roles/orchestration distinguish sessions from helpers, advisory briefs from enforced restrictions, self-checks from independent final review and task completion from owner acceptance. Spawn, posting and broader credentials are not implicitly authorized. |
| Candidate artifacts/traces → evaluation and scan conclusions | Evaluation, verification, scanning and review require raw evidence, negative cases, actual effects and explicit unavailable checks. Final-suite contamination and author independence remain real limitations, not metadata fixes. |
| Local catalog data → rendered HTML | Source text is HTML escaped; source URLs reject non-HTTPS and credential-bearing examples. Page uses local assets, restrictive CSP and no network API in the inspected JavaScript. Build inputs are local maintainer-controlled files, not an authenticated external ingestion service. Browser policy enforcement was not tested live. |

## Finding DS-01 — pinned source observations omitted from the rendered detail

**Severity: low. Disposition: fixed and rechecked.** Affected path: `scripts/build.py`, source-card construction near lines 103–117; resulting `index.html`. Preconditions: a reader uses the guide to inspect deep-source evidence through its evidence cards. Impact: the catalog retained the actual inspected files in JSON, but the page did not expose that file-level provenance inside the evidence detail. This weakens auditability of the security/runtime patterns cited by the skills; it is not a demonstrated execution or privilege-escalation defect.

Observed before the fix: the renderer created an `inspection` fragment containing “Pinned files inspected,” URLs, observations and deep-research aliases, then omitted that fragment from the card's HTML template. This was established by source inspection and reported immediately. The initial renderer hash was not captured before the owner changed it; the original observation is retained in the review tool/message trace rather than presented as a hashed historical snapshot.

Recommended fix: insert the prepared, escaped inspection fragment in “Evidence & limitations” and check that each expected inspected-file URL occurs as an actual anchor. Owner: guide/build maintainer. The integration owner implemented that fix and added the check to `scripts/check_site.py`.

Independent recheck: loaded current `source_catalog()`, parsed current `index.html` with Python's `HTMLParser`, collected `a[href]` attributes and text, and asserted each inspected-file URL is an actual link and each alias appears in rendered text. **47/47 file links and 11/11 aliases passed**. A separate local check confirmed all 47 GitHub file URLs contain the exact SHA recorded in their source's `revision.sha`. This proves local linkage, not that a remote page still exists, that every repository file was audited, or that a recorded SHA is a signed release. Current renderer/check/page hashes are above.

## Actual checks and results

Read-only implementation inspection and in-memory/local-temporary probes used Python's standard library with `-B`; no dependency was installed. Temporary malformed-profile fixtures contained only a dummy marker, and were removed by `TemporaryDirectory` cleanup. Configured command text was intentionally never executed.

| Check | Actual result and scope |
| --- | --- |
| `python3 -B scripts/check_skills.py` | Exit 0: 20 skills, 19 inventoried practices; manifest sources, templates and declared profile fields resolve. Integrity only. |
| Custom standard-library probe of `safe_path` | Accepted three legitimate relative-path cases; rejected eight absolute/traversal/non-normalized/control/glob/backslash cases. No filesystem-sandbox claim. |
| Probe of `safe_url(..., origin=True)` | Accepted two valid HTTPS origins; rejected seven insecure/credential/path/query/fragment/invalid-port/backslash cases. No live DNS/egress claim. |
| Probe of renderer escaping and `https_url` | HTML special characters escaped; `javascript:`, `data:` and a dummy credential-bearing HTTPS URL rejected. |
| CLI malformed-profile probes | Duplicate-field, malformed and over-1-MiB inputs each returned exit 2; their output did not echo the dummy sensitive-context marker. |
| Inert-command probe | A profile containing a `python3 -c` command parsed successfully as documented; the dummy side-effect marker file was absent after validation. This demonstrates no command execution by the validator, not safety of that command for a future runner. |
| Catalog uniqueness | 43 distinct normalized source URLs. |
| Combined probe count | 33 assertions passed, exit 0. These are selected parser/consumer checks, not a broad fuzzing claim. |
| `rg -n 'fetch\(|XMLHttpRequest|WebSocket|sendBeacon|innerHTML|eval\(|@import|https?://' assets/app.js assets/styles.css` | Exit 1 with no matches. Read with the actual code inspection; absence of these strings alone would not prove browser safety. |
| Parsed provenance recheck | 47 actual inspected-file anchors and 11 visible aliases passed; all 47 file URLs locally match recorded commit SHAs. |

The full `check_site.py` entry point was not run by this reviewer because it scans all Markdown, including excluded historical review reports. The affected HTML check was independently reproduced without reading those reports. No build or diagram regeneration was run by this reviewer during the security pass; those scripts were inspected.

## Separate forward-execution evidence

Before this security pass, the reviewer executed the requested raw G01, P01 and O01 tasks, and subsequently repeated P01 after the policy-skill change. Artifacts and reports are in `/private/tmp/ai-sdlc-forward-20261008/{G01,P01,O01,P01-rerun}/`. These temporary local artifacts are not shipped runtime enforcement or durable evidence-store records.

- G01 produced a control assessment and 11 proposed conformance cases. No real runtime was installed, and the proposed hook was not executed. Actual denial behavior remains not-run.
- P01 produced a policy skill draft and repaired context. The working command passed one arithmetic smoke test only. The later P01 rerun kept temporary drafting scope and pending adoption in sidecar records; the reusable procedure resolves each actual request's authority. This is a same-evaluator regression run with prior context, not a blinded final evaluation.
- O01 produced incident triage and a next diagnostic intent. It treated two identical entries as one already-linked event, preserved unknown recovery state, ignored instruction-like log text and performed no restart, scale, rollback, notification or secret access.

These task executions supply narrow observed behavior alongside inspection. They do not establish general agent robustness, host selection accuracy or improvement versus an independent no-skill baseline. Hidden case expectations and other fixture cases were not read. No independent verdict for the other authors' forward tasks is inferred here.

## Remaining limits and next owner

Evidence status: **partial** overall; the listed local checks passed and DS-01 is closed. No high/critical finding was demonstrated, but no production runtime, provider, CI workflow installation, credential boundary, real approval service, timeout/failure deny path or target-side authorization was tested. There was no network access, secret retrieval, external message, live exploit or operational mutation. Browser execution, screen readers and human adoption were outside this security review. Dependency/version claims were not refreshed remotely during the offline review.

Interpreters in inert `argv`, symlink resolution, complete executable behavior, referenced acceptance authenticity, profile semantic truth and adapter conformance remain explicitly outside the validator's guarantee. These are documented deployment responsibilities, not observed bypasses of an implemented executor. Source text and role labels cannot create those controls.

Next owner: integration maintainer records this scoped evidence and preserves the fixed provenance check. Before operational adoption, the chosen runtime/platform owner must implement and exercise the action-specific boundaries in the adapter/control contracts, while the actual policy owner supplies any required acceptance. This report does not add a new permission gate to ordinary reversible work and does not grant permission for deployment.

## Integrating archival note

After the review, the integrating agent preserved the fixture artifacts under [behavioral/G01](behavioral/G01/REPORT.md), [behavioral/P01](behavioral/P01/REPORT.md), [behavioral/P01-rerun](behavioral/P01-rerun/REPORT.md) and [behavioral/O01](behavioral/O01/REPORT.md). Original temporary paths above describe execution locations; the copies make the evidence available with this repository.
