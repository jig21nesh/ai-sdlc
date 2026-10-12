---
name: ai-sdlc-guardrails
description: Design, inspect and test runtime boundaries for agent tools, build hooks or consequential-action approvals. Use when configuring or assessing an actual control, not to treat a prompt or profile as enforcement.
---

# Assess the controls that actually govern actions

Read the [shared contract](../shared-contract.md). This practice supports Build and Deploy. It produces an action/control map and versioned conformance evidence. It ships no universal executor, hook installation or production approval service.

## Select the mode from the authorized task

- **Prepare:** identify required controls and produce a reviewable configuration/test proposal. Use this when no adapter exists or installation/testing is outside scope.
- **Assess:** inspect an existing adapter and exercise authorized isolated fixtures. Begin read-only; execute only reviewed local checks with understood side effects.
- **Change:** implement a narrowly scoped control change only when authorized, preserve a recovery path, and run affected conformance checks before reporting the control effective.

Obtain the action classes, protected data/targets, required outcomes, host/adapter version and actual effective settings. Resolve who owns the control and who can modify it. Missing organization decisions block only dependent consequential actions; continue preparation and unrelated reversible work.

## Procedure

1. **Trace the whole action path.** Map user/event identity through model, tool/SDK, shell, connector, CI and target service. Identify enforcement before effects, observation after effects and every alternate path. Include helpers, imported settings, direct API clients and tools outside a shell sandbox. A post-action hook can detect an event but cannot prevent the event that already occurred.

2. **Separate convenience from authorization.** Formatting and fast build checks can help feedback without being security gates. For each selected invariant, specify the operation, normalized target, parameter constraints, candidate/artifact, credentials and expected allow/deny behavior. Derive it from actual policy and task scope, not a copied sample. Classify each control as enforced, advisory, unavailable or untested, with evidence.

3. **Inspect the concrete adapter.** Record its implementation/digest, runtime version, event/matcher, input and decision schemas, protected configuration, timeout/error behavior and settings precedence. Review how identity, paths, symlinks, URLs, arguments and executable resolution are validated. Substring command matching and an agent-editable environment flag do not establish exact-action authorization. Do not interpolate profile strings into shell commands.

4. **Bind required approval outside the model.** Where actual policy requires it, the trusted component must validate the authorized actor, operation, target, material arguments, immutable candidate/artifact, scope, validity and revocation. Test stale and mismatched decisions. A file claiming approval, a returned tool message or a child's “approved” answer is evidence to authenticate, not permission. Reuse valid existing decisions within their scope; do not invent approval requirements for routine actions.

5. **Construct a safe conformance fixture.** Use temporary files, synthetic data, dummy secrets and a controlled local target. Define the expected permitted/denied effect and an independent observation before running the case. Keep live credentials, production targets and real data outside the fixture. If the real adapter cannot be exercised safely, write the case and record `not-run`; a mock of the adapter is not evidence about the deployed control.

6. **Observe effects, including failures.** Use the [control-assessment record](assets/control-assessment.md). Cover a legitimate allowed action and its nearest prohibited variant; missing/malformed approval; stale candidate; path/link or argument ambiguity; bypass through another tool; and attempts to edit or unload the control. Where relevant, test missing executable, malformed output, nonzero exit, timeout and unavailable approval service. Assert what did or did not happen at the target, not merely that a callback ran.

7. **Evaluate scope and failure disposition.** Compare each observed effect to its requirement. Hook semantics differ by event/type/version: execution failure may continue under ordinary permission handling. For a required pre-action gate, unexpected continuation is a failed control, even if the test action was harmless. Stop using the affected automation for protected actions and report the limitation; do not silently disable the gate or generalize one passing hook to all tools.

8. **Handoff or apply the scoped fix.** If changes are authorized, correct the narrow cause and rerun affected tests within the shared repair limit. Preserve the configuration diff and updated identity. Explain uncovered paths and the owner decision needed. Installation, broader privileges, live rollout and external messages are separate actions unless already authorized. Control changes should also trigger relevant delivery-agent regression cases.

## Adaptation to existing configuration

| Existing field | Use |
|---|---|
| `org.tools.runtime_controls_ref`, `org.tools.authorization_policy_ref` | Locate the actual action/control contract, trusted authority and ownership. |
| `org.tools.allowed_tool_ids`, `org.tools.allowed_read_paths`, `org.tools.allowed_write_paths`, `org.tools.allowed_network_origins` | Identify policy scope to compare with effective enforcement; declarations alone prove nothing. |
| `org.tools.max_agents`, `org.tools.max_task_seconds`, `org.tools.max_task_cost_usd` | Identify measurable runtime budgets across retries and helpers. |
| `org.release.approval_policy_ref`, `org.release.approval_required` | Resolve exact-action approval rules without treating a Boolean as authorization. |
| `org.operations.emergency_stop_process_ref` | Locate authorized stop/recovery behavior. |
| `project.context.adapter_profile_ref`, `project.context.tool_ids`, `project.context.network_origins` | Identify selected adapters and narrower capabilities. |
| `project.workflow.allowed_read_paths`, `project.workflow.allowed_write_paths`, `project.workflow.stop_conditions` | Apply task scope and stop criteria. |
| `project.commands` | Inspect literal argument records, executable behavior, side effects and referenced authority. |
| `project.release.authorization_ref`, `project.release.target_environment_id`, `project.release.provenance_ref` | Bind a release control to the actual target and immutable artifact. |
| `project.quality.eval_suite_refs` | Link regression cases affected by a control change. |

The [adapter example](../../config/adapters.example.json) provides `implementation_ref`, `version_or_digest`, `configuration_ref`, `permission_policy_ref` and `conformance_evidence_ref` under each selected adapter. These are references, not an implemented or validated adapter. Credentials remain in their designated store, never in fixtures or reports.

## Output contract

Deliver the action/control matrix, inspected adapter/configuration identity, control owner and change authority, test cases with observed target effects, evidence locations, uncovered surfaces and failure dispositions. Distinguish proposed settings, simulated behavior and actual runtime results. Include status, residual risk, next owner/action and any concrete change/rollback artifact. State only the protection demonstrated at that version and scope.

## Decision example

A deployment hook searches for a command word and trusts `APPROVED=true`. A wrapper reaches the same deployment API without that word, while a timeout lets execution continue. Record both as control failures if prevention was required; do not “fix” the test by matching only the sample command. Propose a trusted action adapter or target-side authorization that covers the actual paths. Continue preparing a release plan while protected execution remains unavailable.

## Sources and portability

Primary practices: [Anthropic playbook, Build hooks and Deploy approvals](https://claude.com/resources/articles/the-ai-native-sdlc-playbook). Technical behavior must be checked in [hook](https://code.claude.com/docs/en/hooks), [permission-mode](https://code.claude.com/docs/en/permission-modes) and [sandbox](https://code.claude.com/docs/en/sandboxing) documentation for the installed version.

Corroboration: [Agent SDK, DG05](https://github.com/anthropics/claude-agent-sdk-python) motivates effect assertions and event-specific semantics; [Code Action, DG04](https://github.com/anthropics/claude-code-action) motivates tracing actor/token/tool authority; [governance experience, DM04](https://pauldjohnston.medium.com/agentic-development-best-practices-0e23ab07c1f8) supports versioned ownership. Consult [GitHub](../../research/deep-github-sources.json) and [Medium](../../research/deep-medium-sources.json) evidence limits. No source sample is installed by this skill.
