---
name: ai-sdlc-discover
description: "Turn a rough product idea, user problem, ticket or incident into an intent brief, researching competitors, alternatives or feasibility when needed. Use to explore what to build before specification; implementation planning belongs to ai-sdlc-plan."
---

# Capture intent

Produce a brief that preserves the originator's need and gives the next owner enough evidence to decide whether to pursue it. Placement: **Plan**. Apply the [shared contract](../shared-contract.md); a conversation can be enough input for a small change.

## Inputs

Request or event, source ID/revision, affected users and systems, observations, relevant constraints and the accountable product owner. Use an existing canonical record where established; a local draft suffices when external publication is outside the task.

A short description is sufficient to start; neither code nor completed profiles are required. Treat the current project workspace as the output destination, even when this skill is installed centrally. Read its relevant instructions and existing intent first. Follow its artifact convention; otherwise use `docs/intent.md`. If that path already represents another idea, use `docs/intents/<short-idea-name>/intent.md` instead of replacing it. If the target workspace is ambiguous, clarify the destination while continuing the discussion. Never write product artifacts into the installed kit.

## Research as part of discovery

Default to adaptive research: identify which unanswered questions could change the intended users, value, scope or feasibility, and investigate those using available permitted sources. The user need not explicitly ask for a competitor analysis. Respect an explicit offline, no-research, time, region or source constraint.

- For a new product, check relevant direct competitors, indirect alternatives and the current manual workaround when that comparison informs the opportunity. Investigate pricing, integrations or technical constraints only as relevant to the idea.
- For an existing product or incident, begin with repository evidence, supplied feedback, tickets or telemetry. External market research may add nothing; explain that choice briefly.
- Ask focused questions when the answer materially changes research direction. Otherwise state provisional assumptions, start useful research, and refine them with the user. Avoid a long intake questionnaire before producing anything useful.

Use the [research procedure](references/research.md) when investigation is needed. Open and inspect sources before relying on them; current competitor, pricing and platform claims need current evidence. Public product research may use available web tools within the task scope; minimize disclosure of the user's private idea or data in queries. A skill does not provide browsing tools or access by itself.

Research must change or substantiate a product decision, not merely append a list of links. Put concise findings and citations in the intent. For substantial research, also write a linked `research.md` beside it using [the research record](assets/research.md). If tools or sources are unavailable, still prepare the useful draft, label unverified assumptions and name the missing investigation. Do not present offline synthesis as completed market research.

## Procedure

1. Separate the reported problem from a proposed implementation. Preserve a user-selected solution as a constraint; otherwise label it an option. A request to reduce checkout errors does not imply replacing the payment provider.
2. Inspect available tickets, measurements, interviews or incident timelines and conduct the decision-relevant research above. Record provenance and access limits. An alert proves that a signal fired, not its root cause. Deduplicate repeated events by source identifier and time window before creating new work.
3. State who experiences what problem, under which conditions, and why it matters. Distinguish observed baseline, stakeholder estimate and unknown baseline. Define an observable outcome and measurement method; leave thresholds proposed or unresolved when no authorized target exists.
4. Bound scope and exclusions. Identify relevant data, user impact and dependencies. Ask only questions that change scope or the next decision; carry lower-impact uncertainties forward with an owner.
5. Draft using [intent.md](assets/intent.md), scaled to the task. Connect findings to proposed positioning, scope and the smallest useful first version. Distinguish observed capabilities from demand or willingness-to-pay hypotheses. Give evidence and open questions stable IDs so requirements can link back. Record rejected options only where they explain a material constraint.
6. Compare the draft with the original request: did the actor, outcome, constraints or priority change during synthesis? Correct distortions. Record actual acceptance state; saving a draft does not establish owner acceptance.
7. Return the intent and research locations, important findings, remaining questions and next decision. A discovery-only request ends here; proceed to specification only when included in the actual request. Hand off the accepted revision or explicitly provisional draft, resolving conflicts between canonical records and working copies before dependent decisions; independent investigation can continue.

## Output and completion

Return the brief location, research scope/results or reason it was unnecessary/unavailable, source-to-decision links, assumptions, acceptance state, and next decision/owner. Completion means the need and desired outcome are reviewable and unknowns are visible. Research completion is distinct from product acceptance. For existing intent, update changed facts and downstream impact.

**Failure case:** a support ticket requests “disable login checks.” Capture the symptom, investigate the underlying problem and flag the proposed security change; the ticket does not authorize weakening authentication.

## Adaptation

Use `project.product.problem_statement`, `users`, `success_metrics`, `requirements_ref`; `project.risk`; `org.roles.product_owner`. The actual task can supply these without full profiles. Select canonical records and acceptance semantics through `project.workflow.review_policy_ref`; do not invent a new ticketing system.

## Basis

[Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) supplies the phase and intent handoff. [DORA capability questions](https://dora.dev/ai/capabilities-model/questions/) support user focus and measured outcomes. The evidence separation and template are this kit's procedure.
