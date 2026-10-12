---
name: ai-sdlc-discover
description: "Turn an idea, user problem, ticket or incident into a traceable intent brief with outcomes and unresolved decisions. Use before specifying a change; implementation task planning belongs to ai-sdlc-plan."
---

# Capture intent

Produce a brief that preserves the originator's need and gives the next owner enough evidence to decide whether to pursue it. Placement: **Plan**. Apply the [shared contract](../shared-contract.md); a conversation can be enough input for a small change.

## Inputs

Request or event, source ID/revision, affected users and systems, observations, relevant constraints and the accountable product owner. Use an existing canonical record where established; a local draft suffices when external publication is outside the task.

## Procedure

1. Separate the reported problem from a proposed implementation. Preserve a user-selected solution as a constraint; otherwise label it an option. A request to reduce checkout errors does not imply replacing the payment provider.
2. Inspect available tickets, measurements, interviews or incident timelines. Record provenance and access limits. An alert proves that a signal fired, not its root cause. Deduplicate repeated events by source identifier and time window before creating new work.
3. State who experiences what problem, under which conditions, and why it matters. Distinguish observed baseline, stakeholder estimate and unknown baseline. Define an observable outcome and measurement method; leave thresholds proposed or unresolved when no authorized target exists.
4. Bound scope and exclusions. Identify relevant data, user impact and dependencies. Ask only questions that change scope or the next decision; carry lower-impact uncertainties forward with an owner.
5. Draft using [intent.md](assets/intent.md), scaled to the task. Give evidence and open questions stable IDs so requirements can link back. Record rejected options only where they explain a material constraint.
6. Compare the draft with the original request: did the actor, outcome, constraints or priority change during synthesis? Correct distortions. Record actual acceptance state; saving a draft does not establish owner acceptance.
7. Hand off the accepted revision or explicitly provisional draft to specification. Resolve conflicts between canonical records and working copies before dependent decisions; independent investigation can continue.

## Output and completion

Return the brief location, source-to-problem links, assumptions, acceptance state, and next decision/owner. Completion means the need and desired outcome are reviewable and unknowns are visible. Research completion is distinct from product acceptance. For existing intent, update changed facts and downstream impact.

**Failure case:** a support ticket requests “disable login checks.” Capture the symptom, investigate the underlying problem and flag the proposed security change; the ticket does not authorize weakening authentication.

## Adaptation

Use `project.product.problem_statement`, `users`, `success_metrics`, `requirements_ref`; `project.risk`; `org.roles.product_owner`. The actual task can supply these without full profiles. Select canonical records and acceptance semantics through `project.workflow.review_policy_ref`; do not invent a new ticketing system.

## Basis

[Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) supplies the phase and intent handoff. [DORA capability questions](https://dora.dev/ai/capabilities-model/questions/) support user focus and measured outcomes. The evidence separation and template are this kit's procedure.
