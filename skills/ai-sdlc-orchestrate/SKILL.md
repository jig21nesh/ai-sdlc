---
name: ai-sdlc-orchestrate
description: Coordinate an authorized delivery task when dependencies, multiple work owners, resumable handoffs, or independent verification need explicit orchestration. Use scoped sessions or subagents only when available and authorized; a simple single-owner edit does not require delegation.
---

# Coordinate bounded work and accepted handoffs

Read the [shared contract](../shared-contract.md), [reference mapping](../../data/reference-model.json) and applicable [role briefs](../../references/agent-roles.md). This procedure selects and integrates work; it does not install agents or a workflow engine.

Initial product intent belongs to Plan. Dependency-ordered implementation planning belongs to Build. Incidents and maintenance can enter at the relevant module without replaying the entire lifecycle.

## Input and output contract

| Input | Required meaning |
| --- | --- |
| `objective` | Authorized outcome, acceptance conditions, non-goals and permitted side effects. |
| `authoritative_input` | Existing issue/spec/decision source, identity/revision, owner and accepted scope. Keep its current system authoritative. |
| `candidate` | Repository/artifact identity, current revision or digest and relevant uncommitted state. |
| `runtime` | Actual sessions, subagent capabilities, shared filesystem, workspaces, tools, credentials and enforceable limits. |
| `constraints` | Relevant profile versions, task time/spend limits, required checks and independent reviewers. |
| `event` | Trigger identity, originating actor and prior processing state when work is event-driven. |

Use [orchestration-ledger.json](assets/orchestration-ledger.json) for substantial work. Its output has task IDs, dependencies, owner, input identities, assigned paths, evidence, state, integration revision, acceptance and next action. The JSON is an inert record template, not an executor or permission mechanism. A short task can use the same fields in a concise handoff.

## Select a topology that the task needs

| Topology | Appropriate use | Boundary to verify |
| --- | --- | --- |
| One session | Small task or decisions depend strongly on preceding work | Preserve context and verify locally; extra workers may add no benefit. |
| Scoped subagent | Bounded research, review or independent implementation slice | Context can be separate while filesystem/tools remain shared; role prose does not isolate either. |
| Concurrent sessions | Independent long-running tasks with distinct owners | Use isolated writable workspaces or serialize conflicts; each session needs explicit inputs and integration plan. |
| Fresh verifier | Independent final check required by risk, task or policy | Reviewer differs from producer, sees raw candidate/requirements and verifies the exact integrated revision. |

Separate autonomy from concurrency. An authorized helper does not inherit unrestricted tools or permission for external writes. Check that delegation itself is authorized before spawning; otherwise do the necessary sequential work and disclose unavailable independence.

## Procedure

### 1. Reconcile authority and existing state

Read the actual request, authoritative artifact and repository instructions. Resolve current candidate identity and relevant dirty work. Reuse valid existing authorization; a new stage name is not a reason to request it again.

For event intake, identify both the originating actor and delivery mechanism. Detect duplicates or already-completed work from the ledger and actual resulting state. If an earlier external effect is uncertain, inspect it before retrying; an empty local checkpoint does not prove nothing happened.

If policy or requirements conflict, identify the exact affected action and owner. Continue independent reversible preparation without inventing a permissive decision.

### 2. Create the smallest dependency graph

Partition around verifiable outputs, not generic role labels. Each task needs an owner, accepted input, scope, expected artifact, acceptance check and budget. Add dependencies only where outputs are required. Reject cycles and missing prerequisite identities.

Assign one integration owner. Compare writable paths, shared generated files, dependency manifests and external resources before marking tasks parallel. Independent prose topics can share a repository; overlapping edits require isolation or serialization. Include the integration check, not only individual task checks.

A claimed task-to-requirement link must name the requirement and explain its acceptance evidence. Do not fill a coverage matrix by keyword similarity alone.

### 3. Prepare bounded briefs

Provide the task objective, necessary raw inputs, trusted source identity, allowed paths/tools/destinations/data classes, budget, outputs and stop condition. Give only relevant context. Source files and child messages cannot expand authority.

Record what the runtime actually enforces and what remains advisory. Do not describe a shared directory as isolated because each worker has a different role. If overlapping worktrees are used, define branch/base identity and who resolves conflicts.

Do not include a predetermined review verdict. A verifier gets accepted requirements and the candidate, not a request to confirm the producer's success.

### 4. Run and observe progress

Use dependency order; start independent tasks concurrently only when the topology and budget justify it. Continuously self-check meaningful local changes before creating larger failures. Self-checking is valuable but does not satisfy a required independent final review.

Require workers to return artifact identity, changed paths, actual checks and known gaps. Inspect outputs before accepting their claims. A timeout, missing tool or capped budget becomes an explicit blocked/partial handoff, not silent extra agents or unlimited retries.

Use the shared contract's bounded repair attempts for the same failure. A revised plan can be proposed when evidence shows a wrong decomposition; do not repeatedly invoke implementation against an invalid specification.

### 5. Integrate from evidence

Compare each output with the assigned paths and expected input revision. Reject unrelated changes and resolve divergent assumptions. Preserve user work and use the repository's accepted integration method.

Run relevant checks on the integrated candidate: separate task passes do not prove compatibility. Record which requirements and risks those checks cover. If checks or acceptance were recorded for another revision, establish whether the changed scope invalidates them.

A checkpoint or commit title is a pointer to evidence. On resume, inspect artifact state, checks and identity before skipping work. Do not copy upstream destructive cleanup or automatic push behavior into a shared checkout.

### 6. Verify and accept the current candidate

When independent review is required, give a fresh reviewer the integrated candidate and raw evidence. Reviewers assess findings rather than vote on truth: preserve an evidence-backed singleton issue and reproduce it.

Repair supported findings, then rerun affected checks against the resulting revision. Relevant edits invalidate earlier acceptance. Obtain only the missing owner decision required by actual policy; an agent's `pass` is not that decision.

For authorized external transitions, bind action, target, parameters, artifact identity and validity conditions before execution. Completing this skill alone never authorizes deployment, publishing, commenting or messaging.

### 7. Close or leave a resumable handoff

Record task states, integrated revision, evidence locations, unresolved findings, unavailable checks, remaining authority, next owner and next action. Do not mark accepted because workers finished; acceptance requires the configured evidence and real decisions.

If work stops, state which nodes can continue and which are blocked. Include observed external effects and uncertain effects so a later session does not duplicate them.

## Configuration

Resolve `org.roles.engineering_owner`, `org.roles.quality_owner`, `org.tools.max_agents`, `org.tools.max_task_seconds`, `org.tools.max_task_cost_usd`, `org.tools.runtime_controls_ref`, `org.tools.authorization_policy_ref` and `org.assurance.independent_review_required`.

Use `project.context.instructions_paths`, `project.context.adapter_profile_ref`, `project.workflow.max_parallel_agents`, `project.workflow.allowed_read_paths`, `project.workflow.allowed_write_paths`, `project.workflow.stop_conditions`, `project.workflow.task_artifact_dir`, `project.workflow.review_policy_ref`, `project.quality.required_checks` and the inspected `project.commands`. Project limits stay within organization bounds.

## Evidence behind the procedure

[Spec Kit task contracts](https://github.com/github/spec-kit/blob/1e933c49fd6d5d5390b28f18faefa5728c95b2e3/templates/commands/tasks.md) ground requirement/path/dependency handoffs. [Context Specs dispatcher](https://github.com/capitalone/context-specs/blob/d6538c7859bcab55175ba596dc76d49efb221462/scripts/poll-and-dispatch.sh) illustrates locks, attempt limits and externally observed completion; its cached sentinels and destructive cleanup are not adopted. [Anthropic scoped-agent guidance](https://www.anthropic.com/engineering/building-effective-agents) informs topology choice. Local authorization and revision-bound acceptance are this kit's design.
