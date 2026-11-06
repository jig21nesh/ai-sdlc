---
name: ai-sdlc-plan
description: "Plan implementation of an accepted change: inspect the repository, choose an approach, map files and proof, and prepare bounded task handoffs. This is Build-phase planning; use discovery for initial intent."
---

# Plan an implementable change

Produce a plan that another engineer can execute and verify without the conversation.
This skill belongs to **Build**, not Anthropic's initial Plan stage.
Use the [shared contract](../shared-contract.md) for authority, evidence states and repair limits.
Keep a small authorized fix proportionate: a concise task record may contain the whole plan.
Do not demand a separate document or approval when the accepted request and local policy suffice.

## Resolve the work

Read the accepted intent/specification, relevant decisions, current repository state and task scope.
Record the authoritative system, record ID, revision, acceptance evidence and any working-copy link.
If the task is still an unresolved product problem, prepare discovery questions instead of inventing requirements.
If only a detail is unresolved, isolate the dependent step and continue independent planning.

Load actual profiles selected by the owner; the [org](../../config/org.example.json) and [project](../../config/project.example.json) files are examples.
Resolve these existing paths only as needed:

- `project.product.requirements_ref`, `project.quality.acceptance_ref`: intended behavior and proof.
- `project.architecture.overview_ref`, `interfaces_ref`, `decision_record_dir`, `migration_plan_ref`: design constraints.
- `project.context.instructions_paths`, `root`, `adapter_profile_ref`: relevant context and runtime mapping.
- `project.workflow.branch_strategy`, `review_policy_ref`, `task_artifact_dir`: accepted handoff and change process.
- `project.workflow.allowed_read_paths`, `allowed_write_paths`, `max_parallel_agents`, `stop_conditions`: task bounds.
- `project.commands`, `org.tools`, `org.ai`: command definitions, tool/model limits and budgets.
- `org.roles.engineering_owner`, `org.assurance`: ownership and applicable review requirements.

Missing profiles do not prevent reversible repository inspection under established instructions.
Do not convert unresolved example values into permissive defaults or invent reviewers.

## Inspect before choosing an approach

1. Identify the target revision, branch/check-out and uncommitted changes. Preserve unrelated work.
2. Trace the affected user path through entry points, interfaces, state, dependencies and existing tests.
3. Read relevant manifests/lockfiles and package instructions; confirm the actual toolchain version.
4. Check whether the change crosses ownership boundaries, alters data, changes public contracts or touches release controls.
5. Distinguish observed repository facts from assumptions. Record stale references and contradictory instructions.
6. Use read-only analysis initially; inspect command side effects before running a diagnostic or discovery tool.

Do not estimate a filename, API or command as if it were observed.
If the repository is unavailable, return a provisional plan with evidence gaps and clearly conditional paths.
For a bug, include the symptom and a reproducer or an explicit reason reproduction is unavailable.
For a migration, identify state that must survive and backward/forward compatibility constraints.

## Turn the approach into bounded work

1. Choose the smallest coherent change that satisfies the accepted outcome.
2. Compare meaningful alternatives when the tradeoff changes risk, compatibility or maintainability; avoid ceremonial alternatives for trivial edits.
3. Name affected files/components, ordered steps, dependencies, expected outputs and how each step is verified.
4. Include negative paths and a recovery/rollback assessment where the change has persistent or external effects.
5. Separate implementation from its proof: expected results come from requirements and existing contracts, not proposed code alone.
6. Identify tests and tools that exist, checks to add and checks that need an unavailable environment.
7. Record stop conditions: unresolved material specification conflict, lost authority, changed candidate, exceeded budget or observed harm.

Use [the implementation-plan template](assets/implementation-plan.md) when a durable plan is useful.
Put the plan in the designated `project.workflow.task_artifact_dir` or established record system.
Do not replace an authoritative tracker with a new Markdown source of truth without an agreed mapping.
Writing a draft or committing a plan does not itself accept the plan or launch implementation.

## Decide whether and how to delegate

Delegate only when authorized and the work benefits from separate attention or independent execution.
Use the [task brief](../../references/task-brief.example.json) for scope and output details.

| Work relationship | Coordination choice |
| --- | --- |
| Independent reading or source analysis | Parallel helpers can return evidence without editing product files. |
| Disjoint implementation with stable interfaces | Separate writable scopes or isolated checkouts, then one integration owner. |
| Shared interface or overlapping files | Establish the interface first; serialize dependent edits. |
| Independent verification | Provide the accepted behavior and candidate, not a producer's preferred verdict. |
| Runtime cannot enforce requested isolation | Report that limit; choose a smaller or sequential arrangement. |

Each brief names input revisions, required context, allowed paths/tools, output location, dependencies and budget.
Name one integration owner; specify which worker owns every changed file or interface.
A separate context window is not a separate filesystem, sandbox or credential boundary.
Reserve integration work: reconcile outputs, inspect combined changes and rerun cross-component checks.
Do not let a child task expand scope, change policy or accept consequential residual risk for its producer.

## Reconcile and hand off

Before calling the plan ready, check that:

- Every accepted outcome has a task and a proposed observable check.
- Every task has a clear owner or serial execution order, bounded inputs and a completion condition.
- Dependencies refer to available or explicitly pending artifacts.
- Review, migration and integration effort are represented when applicable.
- Required engineering acceptance is evidenced for this revision; existing authorization can satisfy a routine case.

If the accepted specification or repository materially changes, compare it with the plan before dependent work starts.
Revise affected tasks and proof; preserve superseded revisions and identify changed acceptance scope.
Do not restart unrelated completed planning or request an unchanged approval again.

Return: plan location/revision, chosen approach, task graph, ownership, checks, assumptions and blocked dependencies.
State evidence status separately from acceptance and from permission to execute.
The engineering owner is accountable for the approach; the integration owner is accountable for combining delegated work.
A planning-only request ends with this handoff, not source edits, published tasks or background agents.

## Cases the skill must handle

- An accepted small bug fix: produce a short plan and proceed only when implementation is already in scope.
- Two proposed workers touch one schema: serialize the dependency or split after accepting the shared contract.
- A stale path in a specification: inspect the current code and record the corrected mapping, not a fabricated file.
- Missing test environment: plan the required check and name the gap; do not promise a future pass.

Basis: [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), [workflow composition](https://www.anthropic.com/engineering/building-effective-agents).
Practitioner patterns and limits: [DM-P01, DM-P04 and DM-P05](../../research/deep-medium-analysis.md); these procedures are local synthesis.
