---
name: ai-sdlc-govern
description: "Set or assess the operating agreement for AI-assisted delivery: ownership, policy sources, data/tool boundaries, artifact authority and a bounded adoption pilot. Use for onboarding or a material workflow change."
---

# Establish the operating agreement

Cross-cutting practice. Read the [shared contract](../shared-contract.md). Use this when configuring a workflow, not as a mandatory ceremony before every code change.

## Inputs and scope

Identify the intended use, affected people/systems, existing tool/runtime configuration, actual policies and accountable owners. Distinguish AI assisting development from AI in the shipped product. Missing profiles do not prevent reversible investigation; unresolved sensitive-data or consequential execution authority limits those actions.

## Procedure

1. Choose a bounded pilot with an observable outcome, baseline and stop condition. Assess where time/rework is lost before optimizing code generation. Track delivery quality and user outcomes alongside throughput; do not promise universal productivity gains.
2. Inventory data classes, source systems, models/providers, retention/training/residency terms and tool destinations relevant to that pilot. Distinguish verified agreements, assertions and unresolved provider terms. Use references, never credentials, in the record.
3. Assign accountable roles for product acceptance, engineering, policy exceptions, releases and incidents as applicable. One person may hold several roles. Reuse existing decision channels and authorization; agent role names are not organizational authority.
4. For each artifact type, choose its canonical system, immutable/versioned identity, owner and acceptance evidence. Link working copies to that record. If systems coexist, specify reconciliation and which decision resolves a disagreement; a merged draft is not automatically approved.
5. Separate **guidance**, **verification**, and **enforcement**. Repository instructions provide facts, skills guide decisions, checks produce evidence, and the configured runtime/CI enforces access. Inventory actual permissions, credentials, egress, protected settings, audit trails, budget controls and emergency stop. A declaration or successful schema check is not proof of a runtime boundary.
6. Select the least complicated workflow that meets the need: single session, fixed pipeline, bounded agent, or authorized delegation. Define routine actions already allowed and consequential actions needing particular authority. Do not enable an autonomy mode by name alone; route runtime changes to the guardrails skill and conformance tests.
7. Record policy precedence and task-specific unknowns. Limit blocked work to the affected operation; continue allowed analysis/preparation. Define how stale acceptance, expired exceptions, model/tool changes and incidents trigger reassessment.
8. Produce the [operating agreement](assets/operating-agreement.md). Validate supplied profile declarations with the repository validator if using those profiles, then separately collect actual control evidence. Run the bounded pilot and compare outcomes before expanding scope.

## Output and completion

Return decisions, unresolved gaps, exact profile/reference changes, canonical artifact map, pilot plan, control evidence and acceptance state. Distinguish “configured,” “declared,” “tested,” and “authorized.” A proposal can be complete while adoption remains pending.

**Failure case:** an organization profile allows a tool but the task authorizes only analysis. Keep analysis scope; the allowlist does not authorize deployment. Conversely, missing optional profile fields should not block a local documentation edit.

## Adaptation

Start with [TASK-BRIEF.md](../../templates/TASK-BRIEF.md) for one task. Use `org.roles`, `org.data`, `org.ai`, `org.tools`, `org.assurance`, `org.release`, `org.operations` for reusable organizational decisions. Use `project.context`, `project.workflow` for project facts and artifact ownership references. [ADAPTATION.md](../../config/ADAPTATION.md) names the exact locations; fill only relevant fields before the corresponding action.

## Basis

[DORA capability questions](https://dora.dev/ai/capabilities-model/questions/), [NIST AI RMF core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and [OWASP agent security](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) inform readiness and control separation. Governance is continuous toolkit coverage; it is not a seventh Anthropic stage.
