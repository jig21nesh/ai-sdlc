---
name: ai-sdlc-usability-review
description: Evaluate an interface, documentation, skill bundle, or agent handoff through realistic tasks when usability assessment is requested or required. Report observed friction, accessibility coverage and recovery, and recheck authorized fixes; do not substitute generated feedback for user research.
---

# Review usability through real tasks

Read the [shared contract](../shared-contract.md). This practice supports Design, Test and Deploy acceptance, and Maintain feedback. Inspect the actual artifact and the user's intended outcome; a polished screenshot alone cannot establish task success.

## Establish a usable review scope

| Input field | Type and meaning |
| --- | --- |
| `candidate` | Artifact/location, revision or digest, build/environment and changed behavior. |
| `audience` | Intended users, starting knowledge, device/context and supporting research; label assumptions. |
| `tasks` | Concrete starting state, user goal, success condition, important failure and recovery. |
| `platforms` | Supported browsers/devices, input methods, accessibility target and languages relevant to the product. |
| `mode` | Expert inspection, observed user study, skill forward-test, or remediation recheck. |
| `authority` | Permitted tools, test data, writable paths and whether fixes are requested. |

Use [usability-record.json](assets/usability-record.json) for a substantive review. It is a record template, not a browser test or standards validator. For a small change retain the same evidence fields in a brief report.

If audience evidence is missing, state a provisional audience assumption and conduct an expert walkthrough. Do not invent interviews, personas presented as research, user quotes or measured success rates.

## Procedure

### 1. Choose the journeys that decide usefulness

Start with the user's request and affected behavior. Cover first use/discovery, a representative successful task, a relevant error and recovery. Include a returning or constrained user when it changes the workflow. Avoid expanding a narrow correction into a whole-product redesign.

Write observable success before inspecting: the user reaches the correct destination, completes the action, understands the current state and can recover from the specified mistake. “Looks good” is not an acceptance condition.

Record necessary setup and which steps are genuinely available. Use approved synthetic or sanitized data. A role-specific journey should reflect actual permissions, not an administrator's unrestricted session.

### 2. Walk the real artifact

Execute the journey with available tools, recording start state, steps, result, evidence and environment. Check terminology, discoverability, navigation, progress/state feedback, defaults, empty/loading/error states and reversibility at the moment they affect the task.

Follow actual links and execute documented safe commands when authorized. Compare documentation examples with shipped behavior; a command that fails before setup begins is a first-use defect even if another document has the correct flags.

Check whether the implementation explains what is required, what is optional, who owns missing decisions and what happens next. A template must not imply it has configured or enforced the runtime.

If a browser/device is unavailable, inspect markup/code/documents and run appropriate static checks, then label those observations as static. Do not describe a static reconstruction as a completed keyboard, mobile or screen-reader journey.

### 3. Inspect accessibility in the relevant environment

Use the project's actual accessibility target; consult its authoritative criteria when exact interpretation matters. Check semantic landmarks/headings, accessible names, labels, input errors, keyboard order/operation, visible focus, dialogs and announcements relevant to the task.

Check narrow layouts, zoom/reflow, text size, contrast in relevant states and scroll regions. Record actual viewport/device and method. A CSS breakpoint or focus rule is implementation evidence, not a live rendering pass.

For motion or explanatory GIFs, inspect initial state, play/pause, reduced-motion behavior and equivalent text/static information. For progressive enhancement, verify meaningful content and navigation without JavaScript when that is a supported promise.

An automated scan or selected contrast calculation covers only those checks. Do not infer complete conformance, assistive-technology success or usability for all users.

### 4. Review documentation and skill journeys when applicable

For documentation, walk from the first entry point to one successful use. Verify prerequisites, example values, copyable commands, relative paths and expected failures. Distinguish unresolved examples from malformed input and readiness declarations from operational authorization.

For a skill bundle, try a realistic positive request and an adjacent near miss against its description. Check whether a fresh agent can locate the required inputs, referenced assets, profile ownership, expected outputs and stop conditions without prior conversation.

Use independent fresh-agent forward-testing only when available and authorized. Give the evaluator the request and minimum raw artifacts without a preferred answer. A description inspection alone is not measured host routing, and self-execution is not independent verification.

Separate project context from reusable procedure and host installation. A skill folder, role description or JSON example does not prove automatic discovery, spawned agents or constrained tools. Report the exact host behavior that remains unverified.

### 5. Check explanatory evidence and provenance

For diagrams, compare labels and arrows with the claimed source. Keep reference lifecycle stages, local work modules, practice-adoption relationships and runtime dependencies distinct. Mark original synthesis explicitly; a decorative arrow should not invent a mandatory prerequisite.

Check source dates, access limits and where evidence supports an individual practice rather than the entire framework. A partial article, mutable repository branch or inaccessible paywall body cannot justify a broader claim. Static evidence-library search should find the guide's own suggested terms and expose a recoverable empty state.

### 6. Report issues proportional to impact

Record a stable finding ID, affected journey, candidate identity, location, reproducible steps, expected/observed result, user consequence, severity, evidence method and proposed correction. Separate a blocked task, substantial friction, minor friction and subjective preference.

A potential issue without observed reproduction is a hypothesis; identify the missing environment or condition. Do not turn reviewer preference into a requirement or generate arbitrary user feedback to support a visual change.

State strengths that help the user complete the task, but do not let them obscure an actionable failure. Preserve unperformed checks and missing representative-user evidence in the result.

### 7. Fix within scope and recheck the affected journey

Apply fixes only when requested or already authorized. Preserve established product goals and unrelated work. Reproduce the original condition after the change and check neighboring navigation, responsive states and recovery affected by the fix.

Use the shared contract's bounded repair loop. Record before/after identities and actual recheck method. If the reviewer becomes the producer, disclose that role; arrange required independent final verification separately when available.

If a browser or assistive technology remains unavailable, a static fix can be verified statically while the corresponding live journey stays unperformed. Do not convert closure of a code finding into a broader user-experience pass.

## Configuration and output schema

Resolve `org.roles.product_owner`, `org.roles.quality_owner`, `org.assurance.usability_review_required`, `org.assurance.independent_review_required`, `org.data.allowed_context_classes` and relevant `org.tools` scopes.

Use `project.product.users`, `project.product.requirements_ref`, `project.product.accessibility_target`, `project.product.success_metrics`, `project.quality.acceptance_ref`, `project.quality.accessibility_verification_ref`, `project.workflow.allowed_write_paths` and `project.workflow.task_artifact_dir`. Null settings identify missing decisions; ordinary expert inspection can still proceed with explicit limits.

Output: review mode/audience basis; candidate and environment identities; per-journey steps, success criteria, observed result and evidence; findings/severity/disposition; before/after rechecks; unperformed platform/assistive-technology checks; shared evidence status; and separate owner acceptance. Journey status is `pass`, `fail`, `partial`, `not-run` or `not-applicable` with a reason.

Complete when the required scope has inspectable task evidence and proportionate findings, requested fixes are rechecked at the stated level, and remaining coverage/acceptance decisions are explicit.

## Evidence behind the procedure

[Spec Kit's documentation/workflow contract test](https://github.com/github/spec-kit/blob/1e933c49fd6d5d5390b28f18faefa5728c95b2e3/tests/workflows/test_bundled_speckit_workflow.py) demonstrates checking what users read against what ships. [Anthropic's grader](https://github.com/anthropics/skills/blob/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/skill-creator/agents/grader.md) grounds artifact inspection and weak-assertion critique; [Google review guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html) supports inspecting affected user behavior. The accessibility checklist is local review guidance, not a claim that these repositories establish conformance.
