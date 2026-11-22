# Plan: invoice CSV export

**Status:** draft, provisional: no repository was inspected and the specification is not yet accepted
**Decision needed:** engineering owner (not named in the inputs) to name an integration owner, accept the revised task split and authorize delegation before any task starts.
**Next owner:** Product owner for SPEC D1-D3, then the engineering owner
**Specification:** `SPEC.md` draft 1 for I-9 revision 2; `ADR-001.md` draft 1 (proposed)

## Approach

Add an account-scoped read to the existing invoice filter, then build the export route and CSV encoder on top of it, then the keyboard-operable control. Work runs in sequence under one integration owner because each step consumes the previous step's interface. The proposed split in `proposed-tasks.json` is changed: both tasks wrote `tests/test_export.py`, so that file now has one owner.

## Tasks

| ID | Task and files | Requirement | Depends on | Check and expected result |
| --- | --- | --- | --- | --- |
| T1 | Account-scoped filter taking `account_id` as an argument; `src/domain/invoices.py` | R1, R2 | none | Domain test: other account's invoices never returned; module imports nothing from `src/web` |
| T2 | Export route: auth-context `account_id`, first read before headers, streaming, failure handling; `src/web/export.py`, `tests/test_export.py` | R1-R4, R6, R7 | T1 integrated | Route tests pass for each acceptance example; R2 runs through the real filter |
| T3 | CSV encoder per ADR-001 and column set; `src/web/export.py`, `tests/test_export.py` | R5, R8 | T2; SPEC D1, D2, D3 | Round-trip test on the R8 example; row cell count equals header |
| T4 | Keyboard-operable export control and error message; UI file not identified | R9 | T2; UI path | Keyboard walkthrough: Tab reaches control, Enter downloads |
| T5 | Integration: combined diff review, full `tests/test_export.py`, import check, dependency manifest diff | R1-R9, both constraints | T1-T4 | All pass on one revision; manifest shows no vendor or SDK change |
| T6 | Independent verification of the integrated revision against `SPEC.md` | R1-R9 | T5 | Findings from a reviewer who produced none of T1-T4 |

## Risks and recovery

- Cross-account exposure is the material risk; R2 evidence must not stub the filter.
- No stored data changes; a code revert restores prior behavior. Downloaded files are not recalled.
- R7 needs a real HTTP transport; if none is available locally, R7 stays `not-run` and is reported as a gap, not a pass.

## Blocked or unavailable

- SPEC D1-D3 unresolved: blocks T3, and the R4 assertion in T2.
- UI file for the export control not in `repo-map.txt`: blocks T4 scoping and its owner.
- T1's test file is not identified; `repo-map.txt` names only route tests. The integration owner confirms the path on inspection.
- Test command, toolchain version, base revision and working-tree state were not observed: every path above is conditional on `repo-map.txt` being accurate.
- Engineering owner, integration owner and independent-review policy are not named in the inputs.
- Delegation is not authorized: I-9 authorizes local analysis and planning only.

## Delegation

- Topology: scoped workers in sequence, one integration owner; nothing runs in parallel.
- agent-A: T1, writes `src/domain/invoices.py` and the confirmed domain test file only.
- agent-B: T2 then T3, writes `src/web/export.py` and `tests/test_export.py`; sole owner of both.
- T4 owner: unassigned until the UI file is known. T5: integration owner. T6: a reviewer other than agent-A and agent-B, given `SPEC.md` and the candidate, not a verdict.
- Change from `proposed-tasks.json`: T1 no longer writes `tests/test_export.py`; T2 starts only after T1 is integrated.
- Write scopes are advisory: the runtime was not inspected, and a separate context is not a separate filesystem.
- Each brief carries the SPEC and ADR revisions, the paths above, and the stop conditions in the Record.

## Record

- Plan revision: draft 1, working copy at `IMPLEMENTATION-PLAN.md` in the fixture directory; task artifact directory and canonical tracker not identified.
- Base revision: unknown, no repository behind the inputs. Working-tree changes to preserve: unknown.
- Execution boundaries: planning only; no code changes, no agents spawned, no external actions. Budgets and agent limits: not supplied.
- Stop conditions for execution: SPEC or ADR revision changes, a task needs a path outside its scope, the vendor SDK version would change, authority is missing, two failed repairs on one failure.
- No separate orchestration ledger was written; the task table and Delegation section carry its fields. Task states: all pending.
- Evidence status: `not-run`. Acceptance: pending, engineering owner. Permission to execute: not granted.
- Skills: ai-sdlc bundle 0.3.0, `ai-sdlc-plan`, `ai-sdlc-orchestrate`. Author role: delivery agent. Observed 22 Nov 2026, Sydney time.
