---
name: ai-sdlc-design
description: "Assess a consequential architecture, integration or migration choice using repository evidence, tradeoffs, trust boundaries and a decision record. Use for material design uncertainty within a specification, not every routine edit."
---

# Resolve an architecture decision

Placement: **Design**, as a specialist contribution to the combined specification. Apply the [shared contract](../shared-contract.md). Preserve an explicitly chosen stack or architecture unless evidence identifies a conflict to resolve.

## Procedure

1. Frame one decision and the requirements it affects. Inspect modules, interfaces, topology and data flows. Distinguish documented architecture from observed implementation. Identify owners and consumers before proposing a boundary change.
2. Compare the existing design, a minimal viable change and materially different alternatives where useful. Judge them against actual requirements: correctness, operational complexity, security/data boundaries, reliability, relevant accessibility, migration effort and reversibility. Do not invent numerical scores.
3. Walk a concrete request/event through the proposal. Mark identities, authorization, storage, external calls, failures/retries and telemetry. For AI product features add model/tool/data trust boundaries and nondeterministic failure modes; AI-assisted development alone does not imply a product model.
4. Test the weakest assumption with a bounded investigation or disposable spike when authorized. State what it can prove. Mocks can explore shape or control flow but cannot establish real authentication, performance, transactional semantics or operational compatibility.
5. For stateful/infrastructure changes, map current resource/data identity to proposed identity. Describe compatibility windows, backfill/dual-write risks, irreversible effects, restore prerequisites and rollback limits. A code revert may not recover data.
6. Record the decision using [decision.md](assets/decision.md), evidence, important rejected alternatives, unknowns and a revisit trigger. Separate recommendation from actual owner decision. Feed accepted consequences into spec, tasks and verification obligations.

## Output and completion

Return the decision record, affected requirements/interfaces, evidence limits, unresolved high-impact assumptions and necessary changes to spec/plan/tests. Completion means consequences and uncertainty are reviewable; a diagram does not prove feasibility.

**Failure case:** a new event queue changes ordering and introduces duplicates. Require explicit idempotency/order semantics and consumer compatibility evidence before describing it as equivalent behavior.

## Adaptation

Use `project.architecture.overview_ref`, `interfaces_ref`, `data_flow_ref`, `dependency_manifest_paths`, `migration_plan_ref`, `decision_record_dir`; `project.risk.threats_ref`; `project.quality.performance_budgets_ref`; relevant `org.data` and `org.tools`. Follow the actual exception process. Do not select cloud/model vendors from examples.

## Basis

[DORA capability questions](https://dora.dev/ai/capabilities-model/questions/) ground outcomes and small changes. [Google SRE release engineering](https://sre.google/sre-book/release-engineering/) informs repeatability. [Medium research](../../research/deep-medium-analysis.md) supplies qualified integration/migration experience. This is toolkit synthesis within Anthropic's Design stage.
