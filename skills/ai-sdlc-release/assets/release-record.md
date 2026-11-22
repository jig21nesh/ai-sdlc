# Release: <candidate> to <environment>

**Status:** prepared | deployed | failed | blocked | recovered
**Decision needed:** <the exact authorization or decision required, in one sentence>
**Next owner:** <release or service owner>
**Executed:** <what actually ran; "nothing" for a preparation-only record>

## Binding

| Source revision | Artifact digest | Target account and environment | Current state | Requested state |
| --- | --- | --- | --- | --- |

## Readiness gaps
<Only checks, reviews or approvals that are missing, failed or excepted for this candidate. Link the passing evidence in one line.>

## Effects
<Intended and unintended replacements or deletions, data and identity preservation, schema compatibility, drift. Name the preview method and any remote side effect it had.>

## Rollout and recovery
<Numbered steps with the health signal and stop condition for each. State whether recovery is code rollback, data restore or roll-forward, and whether it was rehearsed.>

## Authority
<Source, actor, operation, target, candidate and conditions of the actual authorization. If missing, the decision required.>

## Action journal
<Delete for a preparation-only record. Preserve failed and partial actions; for a timeout, record state inspection before any retry.>

| Time | Actor | Action and run ID | Observed result | Next permitted action |
| --- | --- | --- | --- | --- |

## CI capability plan
<Delete unless CI integration is in scope. One row per gap between current and required behavior.>

| Capability | Current evidence | Required behavior | Proposed change | Validation and remaining authority |
| --- | --- | --- | --- | --- |

<Cover trigger and input trust, token permissions and secret references, pinned versions, required checks, environment gates and recovery. Keep installation, settings, credentials and dispatch marked not-run unless authorized and observed.>

## Record
Release ID · preparation time · mode · release policy version · provenance record · observation times

Never describe a planned action as executed.
