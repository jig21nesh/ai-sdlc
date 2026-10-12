---
name: ai-sdlc-retire
description: "Plan and, when authorized, execute retirement of software, an AI workflow or a model integration, accounting for consumers, retained data, jobs, credentials and closure evidence."
---

# Retire a system or workflow

**Lifecycle extension**, not a named stage or play in Anthropic's six-stage model. Apply the [shared contract](../shared-contract.md). A retirement plan does not itself authorize deletion.

## Procedure

1. Identify the exact system/version/environment and proposed end state: archived, replaced, disabled or deleted. Inventory consumers, upstream/downstream integrations, scheduled jobs, webhooks, agents, model endpoints, storage/backups, credentials, DNS/routes and owners relevant to that system.
2. Check actual retention obligations, legal holds, contractual commitments and transition acceptance. Record unresolved values explicitly. If hold status is unknown, continue the plan but block dependent destructive data disposition.
3. Define the transition: successor compatibility, user migration, read-only/archive behavior, traffic drain, credential replacement and communications. Prepare drafts; send or publish them only within explicit task authority.
4. Sequence reversible disablement and observation before irreversible operations where feasible. State rollback/restore windows, retained backup accessibility, deletion propagation limits and dependencies that can recreate resources.
5. Bind each mutation to its target, candidate/resource identity, scope and actual authority. Preview inventories and deletion candidates; account for preview side effects. Do not execute a generic recursive delete from a template. Stop for an unexpected consumer, target drift, hold or unapproved side effect.
6. Execute only authorized steps with least-privilege tools. Verify resulting state from authoritative APIs/logs where available: traffic stopped, jobs cannot recreate resources, credentials revoked, retained records accessible, approved data disposition completed.
7. Record failures and residual assets. Mark “disabled,” “archived,” “deletion requested” and “deletion verified” separately. Close only when required evidence and owner decisions exist; no claim of universal deletion from one API success.

## Output and completion

Use [retirement-record.md](assets/retirement-record.md). Return the plan or actual execution ledger, dependencies, retained assets/holds, verification limits and next owner. Planning completion and execution closure are separate states.

**Failure case:** deleting the deployment leaves a scheduler that recreates it, and backups remain under hold. Identify both before claiming retirement complete; authorized disablement can proceed independently of blocked backup deletion.

## Adaptation

Use `project.retirement`, `project.architecture.interfaces_ref`, `project.operations`; `org.data.legal_hold_process_ref`, `deletion_verification_process_ref`, `retention_days`; `org.roles.retention_owner`. Select retention periods and evidence requirements from real policy, never a universal default.

## Basis

[NIST AI RMF core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) covers lifecycle governance including decommissioning. The dependency inventory and staged disposition procedure are supplemental toolkit synthesis for software and agent workflows.
