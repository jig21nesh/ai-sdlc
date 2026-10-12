---
name: ai-sdlc-specify
description: "Produce or reconcile a combined requirements and design specification from an intent, including acceptance scenarios, policy conflicts and traceability. Use before implementation planning or when accepted behavior changes."
---

# Specify behavior and design together

Placement: **Design**. Apply the [shared contract](../shared-contract.md). Use one coherent specification; specialist architecture work can contribute decisions without a separate phase for every change.

## Inputs

Intent or equivalent request and its revision/acceptance state, current system behavior, relevant interface/design artifacts, applicable policies and their versions. If intent is provisional, draft the spec with that dependency visible.

## Procedure

1. Read the request and relevant implementation/interfaces. Identify the source of truth for behavior. Inventory applicable policy clauses: data exposure, authentication, brand, accessibility, reliability or domain rules. Apply policy skills whose source and scope are established.
2. Assign stable requirement IDs linked to an intent outcome or identified risk. Describe observable behavior, separating mandatory constraints, proposed choices and assumptions. Define units and conditions for quantitative targets.
3. Design the user/system flow alongside requirements: entry, successful transition, empty/missing state, error, retry/cancel, permission denial and recovery where relevant. Describe API/event/data contracts and existing consumer compatibility. Omit irrelevant UI sections for a non-UI task with a reason.
4. Choose acceptance examples that distinguish correct from plausible-but-wrong behavior. Include boundary/negative cases and needed integration evidence. Specify which boundaries require real or sandbox integration; do not impose a universal ban on mocks.
5. Record policy conflicts with competing clauses and revisions, affected requirement, options, decision owner and blocked behavior. Continue unaffected drafting. Never silently weaken a rule or use model confidence as a decision.
6. Build the [specification matrix](assets/spec.md): requirement → design element → acceptance example → planned evidence. Flag unsupported requirements, missing proof, out-of-scope design, inconsistent terms and vague words such as “fast” without a measure.
7. Record actual acceptance decisions and the canonical revision. When implementation changes behavior, update affected requirements and examples before reusing earlier acceptance.

## Output and completion

Return the combined spec, requirement/acceptance matrix, material concerns and acceptance state. It is ready for planning when required behavior is sufficiently unambiguous, material conflicts are resolved or explicitly scoped out by an authorized decision, and the canonical revision is identified. An unresolved dependency may still permit useful draft work.

**Failure case:** a mock exposes invoices to any signed-in user while policy restricts them to account owners. Preserve the owner requirement, flag the mismatch and require cross-account denial evidence; the mock does not override authorization.

## Adaptation

Read `project.product.requirements_ref`, `accessibility_target`; `project.quality.acceptance_ref`, `performance_budgets_ref`; `project.architecture.interfaces_ref`, `data_flow_ref`; applicable `org.data` and `org.assurance`. Use `project.workflow.review_policy_ref` for canonical records and required reviewers. Local policy supplies obligations; this skill supplies the method for applying them.

## Basis

[Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) anchors combined Design. [Spec Kit](https://github.com/github/spec-kit) provides inspectable cross-artifact analysis patterns; [deep GitHub research](../../research/deep-github-analysis.md) records revisions and limits. The template and decision rules are original adaptations.
