# Operational investigation

Record incident/check ID, service/tenant/environment, mode, owner and observation time. Identify event/ticket/source ID, verified trigger scope, freshness, deduplication outcome and links to existing incidents.

## Impact and observations

| Time/window | Signal/source | Observation | Coverage/freshness | Sensitive-data handling |
| --- | --- | --- | --- | --- |

Separate confirmed user/system impact from reports and hypotheses. Identify current version/configuration, recent changes, telemetry gaps and investigation budget.

## Hypotheses and checks

| Hypothesis | Supporting evidence | Disconfirming check | Risk/cost and authority | Observed outcome | Updated conclusion |
| --- | --- | --- | --- | --- | --- |

## Proposed response

Record runbook revision, target/current state, exact action and parameters, rationale, prerequisites, actor, existing authority, timeout/retry rules, stop/fallback conditions and verification criteria. Record required unresolved decisions; do not invent approval.

## Action and recovery journal

| Time | Action/run ID | Actual actor/target | Result or uncertain completion | Fresh verification | Remaining risk |
| --- | --- | --- | --- | --- | --- |

An action's successful exit does not prove service recovery. For an uncertain outcome, record state inspection before retry.

## Follow-up and handoff

Link evidence-backed intent/change drafts, preventive tests and proposed runbook/skill updates with owners. Record publishing/notification only if authorized and performed. Keep learned-policy proposals separate from their adoption.

State final observed service state, last observation time, evidence status, unanswered questions, unexecuted steps and next owner/action. Use not-run for monitoring or schedules that were only designed.
