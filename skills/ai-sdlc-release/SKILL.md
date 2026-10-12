---
name: ai-sdlc-release
description: "Prepare CI delivery integration, a reviewable release, or an already authorized deployment, binding checks and decisions to the exact artifact, environment, effects and recovery conditions."
---

# Prepare and execute a release within authority

This **Deploy** procedure separates release preparation, authorization and observed execution.
Read the [shared contract](../shared-contract.md) for authority, evidence and repair limits.
A release request may authorize deployment; a review or preparation request does not.
Honor existing authorization within its exact scope instead of asking for the same decision repeatedly.

## Resolve the requested mode and inputs

Identify whether the task is CI integration/preparation, release preparation, an authorized deployment, a rehearsal or recovery.
Load the accepted candidate, requirements/plan, review findings, check evidence and build provenance.
Record the authoritative acceptance record and immutable revision/artifact identity.

Resolve actual profiles; [org](../../config/org.example.json) and [project](../../config/project.example.json) files are examples:

- `org.release.approval_required`, `approval_policy_ref`, `authorized_environment_ids`, `production_deployment_allowed`: applicable release bounds.
- `org.release.rollback_evidence_required`, `org.roles.release_owner`, `service_owner`: recovery and ownership.
- `org.tools.authorization_policy_ref`, `runtime_controls_ref`: actual actor/action controls.
- `project.release.enabled`, `production`, `target_environment_id`, `authorization_ref`: current release scope and decision evidence.
- `project.release.provenance_ref`, `artifact_dir`: provenance and release records.
- `project.release.deploy_command_id`, `rollback_command_id`, `rollout_plan_ref`, `restore_plan_ref`: mechanisms and conditions.
- `project.architecture.migration_plan_ref`, `project.commands`, `context.adapter_profile_ref`: migration and adapter definitions.
- `project.operations.slo_ref`, `telemetry_ref`, `on_call_ref`, `kill_switch_ref`: health, ownership and stop/fallback.

A false `release.enabled` means this profile does not enable execution; preparation may still be useful.
Unresolved critical authority blocks only the affected external action, not preparation of its reviewable evidence.
A non-null authorization path is not proof: inspect the actual decision and its scope.

## Prepare or integrate CI delivery when requested

Use this branch when adding AI-assisted checks, failure triage, build packaging or release stages to an existing pipeline.
Start with an inventory and capability plan; a CI improvement request does not authorize dispatch, publication or production deployment.
Resolve the CI implementation, version and permission policy through `project.context.adapter_profile_ref`; the [adapter example](../../config/adapters.example.json) is only a mapping guide.

1. Inspect existing pipeline files, reusable jobs, triggers, branch rules and runner configuration. Record which definitions are observed and which platform settings are unavailable.
2. Map each trigger to the code/configuration revision it executes, trust level of its inputs, actor/token and permitted outputs. Include forks, pull requests, manual inputs, schedules and chained workflows only where relevant.
3. Separate untrusted build/test execution from privileged delivery. Inspect shared runners, caches and downloaded artifacts as cross-job trust boundaries; do not run contributor-controlled code with deployment credentials.
4. Identify the minimum job token permissions and secret/identity references. Plan short-lived scoped identities where supported; keep production secrets out of ordinary build/agent context and logs.
5. Inventory actions, reusable workflows, containers and agent tooling. Resolve approved immutable versions/digests; for GitHub actions, verify full commit references against the actual upstream repository. Record upgrade ownership.
6. Define job inputs/outputs: build once, retain an identified artifact and provenance, and make downstream checks/release consume that exact artifact. Reject missing, mismatched or stale evidence rather than rebuilding an unreviewed substitute.
7. Map mandatory checks and applicable delivery-agent evaluations from `project.quality.required_checks`, `eval_suite_refs` and `org.ai.evaluation_policy_ref`. Preserve explicit failure/skip/timeout states; AI failure triage is advisory unless a bounded repair workflow is separately authorized.
8. Map environment selection, protection/acceptance, concurrency, credentials and stop behavior to `org.release` and the existing rollout policy. Untrusted event text must not select arbitrary environments or become executable shell instructions.
9. Document capabilities needed for deployment and rollback/restore: artifact access, state inspection, authorized command, health observations, operator and recovery limits. Name missing permissions or platform features as gaps, not assumed controls.
10. Return the observed-versus-proposed capability map, change locations and staged validation plan. When configuration drafting is requested, prepare the scoped patch using the installed provider's schema, leaving unrequested credentials, environment settings and triggers untouched.

Stage adoption as local/static validation, authorized isolated CI evaluation, then separately authorized environment rollout; do not mark later stages executed from a draft alone.
Plan meaningful negative cases: untrusted input on a privileged route, missing check evidence, artifact mismatch, unavailable environment authority, failed agent evaluation and uncertain rollback completion.
Validate syntax and job dependencies locally when feasible. Run a sandbox pipeline only with existing authorization; retain logs and denied-action evidence.
Do not install a workflow, enable a schedule, change branch protections, add secrets or dispatch a run merely because a prepared patch describes it.
For a preparation-only handoff, record external CI configuration, dispatch and deployment as not-run alongside the concrete draft and remaining decisions.

## Bind the candidate and assess readiness

1. Identify source revision, build artifact digest, provenance/build record and dependency/lockfile state.
2. Confirm required reviews and checks refer to that candidate; record failures, missing evidence and accepted exceptions separately.
3. Verify material findings against intent, specification, implementation plan and the actual diff.
4. Record target environment/account/tenant, expected current version, desired version and actor identity.
5. Enumerate persistent effects: data/schema migration, resource replacement/deletion, access changes and external dependencies.
6. Inspect rollout and recovery plans, including incompatible data transformations and rollback limits.
7. Define measurable health conditions, observation window, stop criteria and the accountable service owner.

If the artifact, parameters, target or relevant policy changes, reassess the affected checks and acceptance.
Do not transfer approval for a mutable tag or an old commit to whatever artifact currently occupies that name.
If immutable identity cannot be established, disclose the gap and obtain the required resolution before consequential execution.

## Preview the actual effects

Use only a reviewed project adapter or command and inspect its declared and actual behavior.
Record the preview method, input candidate, current-state observation time, credentials/role, outputs and coverage limits.
Check whether it creates remote resources/change sets, executes hooks, contacts services or reads sensitive state.
A command called `diff`, `plan`, `validate` or `dry-run` is not necessarily free of side effects.
Execute a preview only when its own side effects are within existing authority.
If that authority is missing, prepare a local analysis and a concrete preview request instead of executing it.

For AWS CDK, current `cdk diff` automatic mode can create a CloudFormation change set using the deploy role and fall back to a template-only comparison.
A template comparison and a change-set preview have different fidelity; preserve which method actually ran.
Resource identity changes may cause replacement even when application tests pass.
These are adapter-specific facts, not a requirement to use CDK or copy its options into every project.
Use current provider documentation for the installed tool version.

Before release, resolve unintended replacement/deletion and migration compatibility gaps against policy.
A recovery plan must name the safe action, prerequisites, data implications, operator and success criteria.
A code rollback may not reverse a destructive migration; distinguish rollback, restore and roll-forward.
Rehearsal is useful evidence only when actually performed in an authorized environment.

## Check execution authority at the boundary

1. Match the existing decision to actor, operation, environment, candidate/artifact, parameters and validity conditions.
2. Confirm required organizational acceptance and actual runtime/CI/environment controls.
3. Verify that the deployment path uses the permitted identity and cannot silently change target or artifact.
4. If a missing decision is required, present the prepared release record and exact proposed action for that decision.
5. Proceed without a new prompt when valid existing authority already covers the action and policy requires nothing further.

An editable approval flag, command-substring match, agent verdict or printed hook warning is not sufficient enforcement.
For unattended adoption, require evidence that real denied paths, hook errors/timeouts and credential boundaries were exercised safely.
Do not install hooks, alter protections, grant credentials or enable unattended schedules as a side effect of releasing software.
Do not send notifications unless explicitly authorized by the task or an applicable invoked workflow.

## Execute once, observe and recover within scope

1. Recheck the bound target/current state immediately before execution; resolve material drift.
2. Invoke the approved command via the runtime's literal argument-array API, with bounded time and minimal permitted credentials.
3. Capture execution/run ID, start/end time, actual actor/target/artifact and redacted output.
4. Observe deployment completion and the configured health signals; a successful CLI exit alone does not prove service health.
5. Verify migrations and the resulting version/state against the intended rollout.
6. On failure, apply only the already authorized recovery path whose prerequisites hold; otherwise stop mutation and hand off concrete evidence.

A timeout is an unknown outcome until checked. Inspect provider/pipeline state before retrying a potentially completed operation.
Respect idempotency and retry policy; do not redeploy repeatedly until a dashboard turns green.
If recovery itself changes risk or requires new authority, prepare that exact decision while continuing permitted diagnosis.
Preserve partial rollout state, failures and any containment already performed.

## Deliver the release record

Use [the release-record template](assets/release-record.md) in `project.release.artifact_dir` or the authoritative release system.
Return the applicable CI capability plan/draft, candidate identity, readiness evidence, preview effects/limits, authority source, execution status and observed service state.
Separate preparation `pass/partial` from deployment `not-run/pass/fail/blocked` and recovery evidence.
Name the release owner, service handoff and unresolved follow-up.
Never describe an unrun deployment, recovery rehearsal or notification as complete.

Cases to distinguish: approved commit with a rebuilt different artifact; preview that creates a remote change set; stateful resource replacement; a deployment timeout that actually completed; and a preparation-only request.

Basis: [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), [Google release engineering](https://sre.google/sre-book/release-engineering/), [SLSA provenance](https://slsa.dev/spec/v1.2/).
Adapter corroboration: [AWS diff](https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-diff.html), [resource IDs](https://docs.aws.amazon.com/cdk/v2/guide/identifiers.html), [hook semantics](https://code.claude.com/docs/en/hooks).
CI examples: [GitHub workflow trust and dependency controls](https://docs.github.com/en/actions/reference/security/secure-use), [environment controls](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments). Use the selected provider's actual capabilities; these links do not mandate GitHub.
Practitioner experience and rejected warning-hook example: [DM-P08 through DM-P10](../../research/deep-medium-analysis.md).
