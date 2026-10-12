# S01 — implementation and proposed delegation plan

Placement: Build-phase implementation planning. Input: accepted I-9 revision 2, local SPEC.md draft 1 and ADR-001 proposal. Only local analysis/planning is authorized. **No code change, commit, agent launch or external task publication has occurred.**

The actual repository base revision and dirty state are unavailable. Before implementation, inspect them and preserve user changes. Do not label the supplied file map as code inspection. Use existing organization controls; absent profiles are not a reason to block this local draft.

## Ordered work and proof

| ID | Owner proposal | Work and writable scope if later authorized | Dependency | Proof/exit |
| --- | --- | --- | --- | --- |
| P0 | Engineering/integration owner, not yet named | Inspect actual code/API, instructions, SDK version, test commands and UI entry point; resolve specification D1-D4 with relevant owners. No product edits in this preparation step. | I-9 r2 | Record actual base revision, known paths/commands and accepted CSV/state/schema decisions; separate unresolved work. |
| T1 | agent-A or a single engineer; not launched | Adapt account-scoped filtering in `src/domain/invoices.py` and its route-level authorization cases in `tests/test_export.py`, preserving existing interfaces. | P0 prerequisites relevant to auth/domain confirmed; final CSV rules need not block independent domain work | Mixed-account, missing-auth and malicious account-selector cases; preserve domain→UI prohibition and SDK pin. |
| T2 | agent-B or the same engineer; not launched | Adapt request/CSV streaming in `src/web/export.py`; complete serialization/error cases in `tests/test_export.py`. | T1 output inspected/accepted; D1/D2/D3 resolved | CSV edge cases, empty/missing/error paths and existing API integration evidence. |
| T3 | UI owner to identify | Add or wire keyboard-operable export control and states at the actual discovered UI path. No guessed existing filename. | P0 locates UI; stable route/state contract from T2 | Real keyboard journey, accessible control/status and error recovery; preserve current navigation. |
| V1 | Verifier distinct from producer if applicable policy requires | Review integrated candidate against SPEC and ADR; checks do not mutate production. | T1/T2/T3 integrated | Required evidence tied to final revision; gaps and negative outcomes retained. |

## Shared-file ownership and integration

The supplied tasks both write `tests/test_export.py`, and T2 already depends on T1. Keep that dependency and **serialize the shared-file edits**. T2 starts only after the integration owner inspects T1's actual output and passes its resulting revision. Separate worktrees would not remove the logical conflict; explicit integration is still required.

A single engineer/session is sufficient for this small connected feature. If later delegation is authorized, disjoint reading may be parallel but implementation follows dependencies. One named integration owner owns the combined candidate and reconciles interface/test changes. Each brief needs base/input revisions, allowed files/tools, expected artifact, actual checks, stop conditions and a runtime-enforced budget. Those runtime details and budgets are currently unresolved; no worker is spawned.

## Stop and failure behavior

Pause only dependent implementation for material uncertainty: CSV expectations unresolved, authority scope changes, user changes would be overwritten, account isolation breaks, SDK changes become necessary, or UI/domain boundaries conflict. Preserve a failing check rather than deleting it. An unavailable billing integration is a disclosed gap; do not silently replace a policy-required integration with a mock.

Integration verifies requirement-to-check coverage, dependency diff, domain imports, cross-account denial, CSV expectations and keyboard states. Authentication and stateful streaming behavior cannot be proved by a proposed mock alone. No test commands, product candidate or live UI were supplied; tests and keyboard verification are not-run.

## Handoff and acceptance

Plan status: partial but useful. Accepted scope is I-9 r2; final spec, ADR recommendation and concrete implementation plan remain drafts. Next action is P0 plus the CSV/schema/state decisions, then execution only if subsequently requested. No production/release authority is implied. See delegation-plan.json for machine-readable task state.
