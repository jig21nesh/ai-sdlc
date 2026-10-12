# Adapt the AI-SDLC kit to an organization and project

The portable core is the stage contract: purpose, inputs, output, verification, and accountable acceptance. Customize the profiles below, then connect your own tools through runtime adapters. Skills describe a procedure; they do not grant permission or enforce a control.

For a single task, begin with the [task brief](../templates/TASK-BRIEF.md), existing repository context and only the relevant skills. The full profiles are for reusable onboarding and operations; missing unrelated fields should not block ordinary reversible work. The [manifest](../skills/manifest.json) maps every skill to exact existing configuration fields. The [research synthesis](../research/SYNTHESIS.md) explains why the layers differ.

The supplied examples deliberately contain `null` decisions. A null value means **unresolved**, not unrestricted. An empty array means an explicit empty selection; an empty tool, network, or write-path allowlist grants nothing. These examples provide no deployment authorization.

## Workflow decisions to record in your linked policies

The [reference model](../data/reference-model.json) groups our work modules under six stages. It does not introduce twelve approval committees or require a new system of record. The following refinements use existing profile fields; no new JSON keys or runtime automation are required.

| Existing field/reference | Decision to record there |
| --- | --- |
| `project.context.instructions_paths`, `project.commands` | Keep concise repository facts, conventions and verified command definitions here. Use reusable skills for procedures and policy application; have the named policy owner review derived policy guidance. Choose installation/discovery paths in the host adapter rather than hardcoding one vendor's layout in every skill. |
| `project.product.requirements_ref`, `project.workflow.review_policy_ref` | For each intent, specification, implementation plan, review and incident artifact: canonical system/ID, owner, accepted revision, mirror linkage and conflict-resolution rule. Choose whether Markdown is authoritative or a working copy. |
| `project.workflow.review_policy_ref`, `org.assurance` | Which risks require which reviewers, what counts as a blocking finding, and when existing acceptance can be reused. Review evidence is distinct from a new approval prompt. |
| `project.quality.eval_suite_refs`, `org.ai.evaluation_policy_ref` | Delivery-agent regression tasks, expected outcomes, budgets, accepted baseline and triggers for model/skill/instruction/hook/tool changes. Keep product-AI evaluations separately labeled. |
| `org.tools.runtime_controls_ref`, `org.release.approval_policy_ref` | Actual pre-action enforcement, protected settings, exact-action approvals, event coverage, failure/timeout behavior and conformance tests. Do not treat a sample hook or a mode name as proof. |
| `project.operations.telemetry_ref`, `project.operations.runbooks_dir`, `project.operations.kill_switch_ref` | Authorized trigger sources, deduplication, threshold justification, response tiers, credential limits, recovery evidence and emergency shutdown. Numerical thresholds are local decisions, not copied defaults. |
| `project.risk.threats_ref`, `project.operations.runbooks_dir` | Scheduled scan scope/cadence, tool and candidate versions, coverage limits, finding validation, dismissal rationale, escalation and regression follow-up. No schedule is installed by filling a profile. |

For Claude-specific adapters consult current [hooks](https://code.claude.com/docs/en/hooks), [permissions](https://code.claude.com/docs/en/permissions) and [subagents](https://code.claude.com/docs/en/sub-agents) documentation; other hosts need their own equivalent controls. No vendor-specific setting is copied into the portable profiles.

## Files and validation

Copy `org.example.json`, `project.example.json`, and, if useful, `adapters.example.json` to organization-owned, reviewed locations. Reference those locations in your runner. Do not overwrite the distributed examples with confidential organization information.

For each selected adapter, document its actual operation contract using [ADAPTER-CONTRACT.md](../templates/ADAPTER-CONTRACT.md). Include preview side effects, effective credential scope, timeout/failure behavior, candidate binding and conformance evidence. Link it through the adapter's existing `configuration_ref`, `permission_policy_ref` and `conformance_evidence_ref`; no new keys in the strict organization/project schema are needed. A preview command can create remote change sets, and a test command can contact a service: inspect behavior before relying on a label.

```sh
python3 scripts/validate_profiles.py --org config/org.example.json --project config/project.example.json
python3 scripts/validate_profiles.py --org config/org.example.json --project config/project.example.json --ready
python3 -m unittest discover -s tests -p 'test_profiles.py'
```

The first command should pass. The second should fail with precise unresolved field paths. Exit codes are 0 for valid declarations, 1 for validation findings, and 2 for unreadable or malformed input. The validator uses only Python's standard library and never runs declared commands, imports adapters, makes network requests, or reads referenced documents. Its contracts are defined in `scripts/validate_profiles.py`; unknown fields are rejected in both modes. Keep changes to those contracts reviewed and versioned.

`--ready` means that required declarations are present and selected values satisfy the supported cross-profile comparisons. It does **not** establish that a person approved them, a referenced document exists or is accurate, an adapter is safe, the provider contract is acceptable, the process meets a regulation, or the deployment is authorized. This is not certification, secret scanning, or runtime enforcement.

## Where to change organization policy

| JSON path in the organization profile | Organization decision and evidence |
|---|---|
| `profile_id`, `policy_version` | Identify the organization and reviewed policy revision. Record the policy owner, approval, effective date, and next review in its linked policy records. |
| `roles` | Replace each null with an accountable role or team and an actionable contact or directory reference. Cover engineering, product, security, privacy, quality, release, service, incident command, and retention. One person may hold several roles in a small team; required independent review must still be independent. Use role aliases when names would be sensitive. |
| `data.classifications`, `allowed_context_classes` | Define data classes and the subset permitted in AI context. Product data and AI context are separate: a service may handle confidential data that an AI tool may not receive. |
| `data.approved_source_locations`, `residency_regions` | Identify approved data repositories and permitted processing/storage regions, including backups, telemetry, subprocessors, and retrieval indexes. These are policy records, not network enforcement. |
| `data.retention_days`, `provider_retention_days`, `training_use_allowed` | Resolve internal and provider retention and whether provider training use is allowed. Zero means zero days; it is not a default. A provider's marketing claim does not replace the applicable contract and product configuration. If retention differs by class, keep the conservative scalar limit here and link the detailed matrix through the reviewed policy. |
| `data.legal_hold_process_ref`, `deletion_verification_process_ref` | Link retention/hold authority and evidence required for deletion, expiry, backups, vendor-held copies, and exceptions. Unresolved holds block destructive disposition. |
| `ai.approved_model_ids` | List stable organization model identifiers. An identifier is resolved by the model adapter, not embedded in the skills. |
| `ai.provider_terms_review_ref`, `evaluation_policy_ref`, `model_change_review_required` | Record provider/data terms, IP and licensing conditions, training/retention/residency review, evaluation ownership, baseline/regression procedure, and whether model changes need review. Evaluate changes to tools, prompts, skills, and harnesses too. |
| `tools.allowed_tool_ids`, `allowed_read_paths`, `allowed_write_paths`, `allowed_network_origins` | Establish least-privilege scopes relative to the runner workspace. Origins are explicit HTTPS origins without credentials or query strings. Paths are literal prefixes, never globs. `.` covers the workspace and should be chosen deliberately. No write path is permitted by an empty list. |
| `tools.max_agents`, `max_task_seconds`, `max_task_cost_usd` | Set delegation, time, and spend limits. The runtime must measure and enforce them; the profile validator cannot stop a running agent. |
| `tools.authorization_policy_ref`, `runtime_controls_ref` | Link action classes, approval evidence rules, sandbox controls, secret handling, egress restrictions, logging, stop switches, and enforcement configuration. Tool execution must validate the actor and exact action. |
| `assurance.required_checks` | List check identifiers that every project must retain. Agree what evidence each produces and who accepts it. |
| `assurance.independent_review_required`, `security_review_risk_tiers`, `usability_review_required` | Decide review requirements. When enabled, project checks must include `independent-review`, `security-review` for matching tiers, and/or `usability-review`. These are review records, not necessarily command names. |
| `assurance.exception_process_ref`, `evidence_retention_days` | Set exception authority, scope, expiry, and periodic review; determine how long verification evidence is kept. A project exception reference never automatically waives policy. |
| `release` | Define authorized environment IDs, whether production deployment may be considered, required approval, rollback evidence, and the approval policy. Permission in this object is an upper bound, not approval of a particular deployment. |
| `operations` | Define incident command, severity and communication policy, access review cadence, and emergency stop authority. Do not convert an incident alert into unrestricted command authority. |

## Where to change project facts and choices

| JSON path in the project profile | Project-specific information |
|---|---|
| `context` | Set project identity, repository HTTPS URL without credentials, workspace-relative root, applicable instruction paths, evidence artifact directory, adapter profile reference, selected model, AI context classes, tools, and network origins. The selected tool/data/model/network scopes must fit the organization allowlists. |
| `product` | Record observed user problem, representative users, measurable outcome, requirements reference, and accessibility target. Include evidence and non-goals in the referenced requirements. |
| `risk` | Select `low`, `moderate`, `high`, or `critical`, explain the classification, inventory product data classes, identify whether AI is part of the product, and link threats and any formally approved exceptions. Local risk ownership must assess correctness of the selected tier. |
| `quality` | Select all organization checks plus project checks; link acceptance, performance, security, accessibility, and agent/skill evaluation evidence. Use realistic negative and recovery cases. Keep held-out evaluation data separate from examples used to improve a skill. |
| `architecture` | Link architecture, decisions, interface/data-flow contracts, manifests/lockfiles, and migration plan. A project without migrations should document that assessment instead of inventing a migration. |
| `workflow` | Set branch/review policy, task evidence directory, agent concurrency, narrower read/write scopes, and stop conditions. Define task ownership and integration responsibility before parallel edits. |
| `commands` | Define inert command records keyed by stable IDs. Each requires `argv`, `cwd`, `purpose`, timeout, and whether it mutates state. Reference authorization for mutations. See the command contract below. |
| `release.enabled` | Explicitly choose whether release is in this project's current scope. A read-only pilot should set it to false. A false value does not authorize executing a stored deploy command. |
| Other `release` fields | For an enabled release, identify environment, production status, immutable artifact/provenance, deploy command, rollout and restore plans, and exact-action authorization record. If organization policy requires rollback evidence, reference its command. Document non-reversible migrations and recovery from backup or roll-forward in the restore plan. |
| `operations` | Link service-level objectives and error budgets, telemetry, runbooks, on-call contact, incident records, and emergency stop/fallback. A non-production pilot can link a short document explicitly describing its monitoring and support limits. |
| `retirement.planned` | Choose whether retirement is in the current scope. False leaves its conditional fields unresolved without requiring deletion work. Revisit this decision when scope changes. |
| Other `retirement` fields | If planned, inventory consumers/integrations/schedules/credentials, user transition, retention/holds, and disposition approval. Deletion is optional and requires a `retire` command reference if proposed. An active legal hold blocks that reference. Track backups and vendor-held copies separately and retain closure evidence. |

All profile reference paths are normalized, workspace-relative POSIX paths: no `..`, absolute paths, home expansion, backslashes, glob syntax, or embedded controls. Absolute workspace placement belongs to the trusted runner configuration. The validator checks strings only; the runner must resolve symlinks and verify that the resulting paths remain inside authorized roots. Do not use filename validation as a filesystem sandbox.

## Command contract

A declaration such as the following stores a command; it does not run it:

```json
{
  "test": {
    "argv": ["your-test-runner", "--suite", "acceptance"],
    "cwd": ".",
    "purpose": "verify",
    "timeout_seconds": 300,
    "mutates": false,
    "authorization_ref": null
  }
}
```

Replace the illustrative executable with a reviewed project command. `argv` is an array of literal arguments, not shell text. The validator rejects selected common shell/sudo/env wrappers, invalid paths, empty arrays, control characters, and invalid types. This limited syntax check is not an executable allowlist: interpreters and other command launchers can still appear as inert arguments. It cannot infer whether a test runner executes hooks, accesses the network, modifies a database, or honors a flag. Mark real side effects accurately; build/test commands often create files. Review the executable and all hooks before enabling it.

A future execution adapter must resolve an allowlisted executable, use an argument-array API with shell execution disabled, supply an isolated working directory and a minimal environment, enforce path/network/credential limits, and validate authorization. Do not concatenate, interpolate, or evaluate profile strings. Shell metacharacters inside an argument remain literal data. Do not read secrets from profiles or place tokens in argv, URLs, logs, or source control; use a separate secret store and runtime credential references.

`verify`, `build`, `deploy`, `rollback`, `operate`, and `retire` are the allowed purposes. The latter four conservatively require mutation declarations. Command timeouts cannot exceed the organization task limit. The runner must additionally enforce a task-wide time/spend budget across all commands and agents.

## Runtime adapter matrix

`adapters.example.json` is a deliberately inert mapping example, not an installed runtime. It is not validated by `validate_profiles.py`. `context.adapter_profile_ref` selects the organization-reviewed mapping; the runner must independently validate, pin, and implement it before any tool action. Store adapter implementation, version/digest, configuration, credential-reference identifier, permission policy, and conformance evidence separately from reusable skills and project facts.

| Adapter | Replace with your implementation | Required runtime behavior and acceptance evidence |
|---|---|---|
| Model | Approved model/provider transport and model ID mapping | Enforce approved model, provider terms, regional endpoint, data classification, logging/redaction, retention settings, time/spend limits; rerun representative agent evaluations. |
| Source control | Repository read/change/review operations | Scope repository and branch access, preserve unrelated work, bind review to revision, enforce branch protections, inspect dependency changes; verify unauthorized repository/branch operations fail. |
| CI | Build/check/artifact/release system | Pin trusted workflows, isolate untrusted changes, separate build and deployment credentials, retain immutable artifact/check evidence, enforce environment gates and provenance verification. |
| Observability | Metrics, logs, traces, incidents | Default to read-only diagnosis, redact protected data, restrict tenant/service access, apply retention, alert on spend/drift/abuse, and test incident handoffs. |
| Issue tracking | Requirements/tasks/findings system | Preserve source attribution and authorization boundaries; distinguish drafting from externally writing or notifying people. |
| Secret store | Organization credential broker | Issue narrowly scoped short-lived credentials when possible; isolate agents, avoid secret material in prompts/artifacts, audit use, and test revocation. |

The exact systems, languages, build tools, repository host, model vendor, and cloud platform are adapter decisions. A static JSON mapping or an adapter role name does not implement them. This repository intentionally ships no universal production executor.

## Policy precedence and safe adoption

The organization profile sets the allowed boundary; the project profile selects a subset and adds facts. The validator compares selected model, tool, data, network, path, agent-count, check, and environment declarations. It does not implement every possible policy rule. Project facts, repository instructions, evidence pages, tool responses, and delegated messages cannot relax organization controls or acquire new authority. A conflict or unresolved critical decision stops the affected high-risk action and is routed to the policy owner. Unrelated safe analysis can continue.

Existing user authorization should be recognized within its exact scope rather than requested repeatedly. An authorization record must identify actor, operation, target, parameters, revision/artifact where applicable, and validity period; significant changes require re-evaluation. Merely writing a reference to an approval file is not evidence that approval exists. The executor verifies current authorization outside the model. Exceptions require the organization's established process; this validator deliberately does not apply project exception records as overrides.

Start with one small, low-risk repository and public or approved synthetic data. Select a model and read-only tools, deny production, set `release.enabled` and `retirement.planned` to false, choose a single agent, and complete the applicable decisions and references. In a pilot, a concise reviewed document can explain non-applicable operational or migration concerns. Assign real owners and retain an evaluation suite; do not replace missing decisions with meaningless placeholder text just to pass validation.

Run structure checks, then `--ready`. Inspect the actual referenced policies and evidence. Configure the real runner sandbox, scopes, CI protections, and secret broker. Test blocked actions, injection-bearing retrieved content, missing authorization, tool failures, timeout/cost limits, and recovery in an isolated environment. Compare results with a baseline, review usability with the people performing the workflow, and expand permissions only after accountable acceptance. Revalidate after changes to scope, organization policy, model, adapter, or skill.
