# Release record

Record release ID, preparation time, mode, release owner and service owner. A completed preparation record does not imply deployment.

## CI integration and capability plan, when in scope

Record current provider/adapter version, pipeline revision, inspected configuration paths and unavailable platform settings. Distinguish observed state from proposed configuration.

| Trigger/job | Executed code/configuration revision and input trust | Runner/cache/artifact boundary | Token permissions and secret/identity references | Allowed output/environment |
| --- | --- | --- | --- | --- |

| Capability | Current evidence | Required behavior | Proposed file/platform change | Owner | Validation and remaining authority |
| --- | --- | --- | --- | --- | --- |

Cover pinned actions/workflows/container/tool versions; build and artifact identity; provenance; required checks and delivery-agent evaluations; failed/skipped/timeout handling; environment gates; concurrency; secret isolation; deployment and recovery capabilities. Record upgrade ownership and missing platform features.

Link the requested draft/configuration patch and its revision. Record the stages separately: local/static validation, authorized isolated CI evaluation, environment rollout. For each, give evidence status and the decision needed to proceed. Include negative cases for untrusted privileged execution, stale or missing checks, artifact mismatch, environment authority, agent-evaluation failure and uncertain recovery.

Keep external installation, platform settings, schedule enablement, credential provisioning, pipeline dispatch and deployment explicitly not-run unless authorized and observed. A draft is not an installed control.

## Immutable binding

| Source revision | Artifact digest | Build/provenance record | Target account/tenant/environment | Expected current state | Requested next state |
| --- | --- | --- | --- | --- | --- |

## Readiness and authority

Link required check/review results for this candidate, remaining gaps, accepted exceptions and release policy version. Record the actual authorization source, actor, operation, target, candidate, parameters, validity and conditions. If missing, state the exact decision required.

## Preview and migration effects

Record preview command/adapter/version, method, observation time, remote side effects, role, created preview resources and evidence limitations. Enumerate intended and unintended replacements/deletions, identity/data preservation, schema compatibility and drift.

## Rollout and recovery

Name steps, prerequisites, health signals, justified observation windows, stop criteria, recovery operators and permitted fallback. Distinguish code rollback, data restore and roll-forward. Record rehearsal evidence or not-run status and remaining risk.

## Action journal

| Time | Actor | Bound target/artifact | Action/run ID and parameters | Observed result | Unknown/partial state | Next permitted action |
| --- | --- | --- | --- | --- | --- | --- |

For timeouts, record state inspection before retry. Preserve failed or partial actions.

## Result and handover

Separately state preparation, deployment, migration, recovery and health-verification evidence statuses. Identify actual resulting version/state and observation time. List service owner, authorized communications performed, unresolved risks and follow-up. Never describe planned actions as executed.
