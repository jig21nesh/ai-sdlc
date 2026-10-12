# Change packet

Use the relevant sections for the actual change. Mark a section not applicable with a reason rather than fabricating evidence. Keep sensitive data out of this artifact and link to access-controlled evidence when needed.

## Identity and authority

Record the task, accountable owner, candidate revision/artifact digest, user-authorized scope, organization/project/adapter profile versions and risk tier. For each artifact identify the canonical system, record ID, accepted revision and any working-copy link; resolve disagreement before dependent work. Distinguish an owner decision from a model recommendation. Bind consequential authorization to the exact action and target.

## Problem and acceptance

State the users, observed problem, source evidence, baseline outcome, requirements with stable IDs, acceptance scenarios and non-goals. Record unknown assumptions and who will resolve them.

## Design and risk

Link architecture decisions, interfaces, data flows, trust boundaries, threat/abuse cases, privacy/accessibility requirements, dependency/license decisions and migration/rollback design. Each unresolved material risk needs an owner and disposition.

## Delivery and verification

Record the implementation plan's affected files, ordered tasks, risks, proof and accepted changes; task dependencies; scoped agent briefs; modified artifacts; and actual test/evaluation results. Map requirements and risks to checks. Include negative cases and relevant performance, accessibility, security and recovery checks. Distinguish continuous self-checks from required independent candidate verification. Record delivery-agent regression evidence when its configuration changes, regardless of whether the product contains AI. For product AI add model/prompt versions, evaluation data provenance, repeated-run outcomes, grader calibration and cost.

## Independent reviews

Record reviewer identity/role, reviewed revision, coverage, findings, severity and supporting evidence. Link fixes and affected rechecks. Preserve unavailable checks and residual risk. Producer self-review does not replace a required independent acceptance decision.

## Release and operations

If applicable, record the immutable artifact, provenance, approvals, destination, migration steps, rollout/stop conditions, rollback or restore evidence, SLOs, dashboards, incident escalation and operational handover. Do not deploy or send messages solely because this template includes a section for them.

## Learning and retirement

Compare outcomes to the baseline and record follow-up owners. Track skill/policy/model changes and regression evidence. For retirement include consumers, scheduled tasks, integrations, credentials, data/backups, retention/holds, approved disposition and closure verification.

## Final handoff

List outputs and their evidence status (`pass`, `fail`, `partial`, `blocked`, `not-run`, `not-applicable`), acceptance decisions separately, known gaps, next owner and next action. Evidence status never grants execution authority.
