# Medium implementation evidence for the six-stage AI-SDLC

Reviewed 2026-10-08. The governing lifecycle is Anthropic's **Plan, Design, Build, Test, Deploy, Maintain**, with non-linear feedback and artifacts connecting the work. Implementation planning belongs inside Build. Medium supplies examples and pitfalls; it does not override the reference model or current runtime documentation. [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook)

The [source register](deep-medium-sources.json) rechecks the original seven records and adds five distinct implementation/operational perspectives. Eleven bodies were accessible; DM07 remains a member-only introduction and contributes no implementation recommendation. `phases` uses Anthropic's six labels; `stages` retains the earlier toolkit module IDs for compatibility. `practice_ids` identifies the original synthesis below. Dates distinguish publication from access; DM12 identifies its earlier original publication.

The practical gap in the first analysis was procedural detail. A reusable skill needs a trigger, authoritative inputs, actual steps, evidence and failure behavior. A recommendation such as “use context” is not sufficient. The following contracts are this toolkit's engineering synthesis, intended for local evaluation rather than claimed as a vendor standard.

## Plan: capture intent without manufacturing requirements

**DM-P01 — evidence-bearing intake.** DM02 provides a role-handoff example, with structural checks and content critique treated separately. Its single-project account does not validate a universal agent count or workflow. [DM02](https://medium.com/@brettluelling/i-replaced-my-sdlc-with-ai-agents-heres-the-framework-that-actually-worked-fcfbfa5e72d0)

The intake skill should:

1. Identify the originating request, ticket or incident, its revision, owner and access restrictions. Use an existing authoritative system where appropriate.
2. Preserve the stated problem, affected users, desired outcome and exclusions. Mark inferred goals and unresolved conflicts explicitly.
3. Separate acceptance of the problem from acceptance of a proposed solution. Record who accepted the handoff under the organization's existing authority model.
4. Produce a linked intent record. Structural validation checks required fields and references; a semantic check asks whether the next role could explain the problem without reading the conversation.

**Adaptation:** authoritative tracker, acceptance owner, sensitive-data rules, problem-size threshold and evidence location. **Failure evaluation:** a vague onboarding request must not silently become a requirement to collect a new personal-data field. If a disputed requirement remains material, route that decision; proceed with independent authorized work.

## Design: specify behavior and structural constraints

**DM-P02 — testable constraints; DM-P03 — architectural boundaries.** DM03 is general advice; DM08 adds a concrete retrospective about functionality masking structural problems. The durable lesson is to review relationships and future change as well as immediate behavior. [DM03](https://medium.com/@dave-patten/the-new-engineering-stack-specs-context-and-agents-f3454529768e), [DM08](https://medium.com/lifefunk/beyond-it-works-why-ai-assisted-development-still-needs-architectural-discipline-7a0b3d3f99ea)

The design skill should:

1. Load accepted intent, applicable policy, current architecture and relevant accepted decisions; identify stale or contradictory inputs.
2. Define observable behavior, error cases, accessibility needs and measurable nonfunctional expectations. An unknown threshold remains an open decision rather than a fabricated number.
3. Compare proportionate options. Describe changed boundaries, dependencies, interface contracts, data ownership and failure behavior. For a significant decision, record context, consequences and its accountable owner.
4. Produce a specification, acceptance scenarios and decision references; identify which checks will establish conformance. Preserve superseded decisions instead of rewriting accepted history invisibly.

ADR mechanics are supported by [AWS's primary ADR guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html). **Adaptation:** architectural invariants, performance budgets, design system, data classification and specialist ownership. **Failure evaluation:** a working background export must fail review if its shared domain module acquires an unauthorized dependency on the web UI.

## Build: prepare a bounded plan and preserve repository context

**DM-P04 — scoped context; DM-P05 — bounded handoffs.** DM01 describes dependency-aware slices and verification signals. DM12 contributes wrong-folder edits and legacy/tool-version mismatch examples. These support loading relevant facts, not assuming that a large instruction file makes execution safe. [DM01](https://medium.com/capital-one-tech/new-open-source-context-specs-released-1f65bfa9db9f), [DM12](https://dius-au.medium.com/a-week-with-claude-code-lessons-surprises-and-smarter-workflows-47584eb55e8d)

The planning and implementation skills should:

1. Inspect the working state, target revision, relevant package ownership, pinned toolchain and existing tests. Record pre-existing user changes before editing.
2. Name affected files, ordered tasks, dependencies, risk, proof and stop conditions. Check the plan against accepted intent and design.
3. Delegate only useful independent work. Each handoff names its base revision, writable scope, inputs, output artifact, checks, budget and return condition. Parallel research does not imply parallel writes are safe.
4. Implement a bounded slice, run the relevant checks, inspect the diff and reconcile deviations with the plan. Preserve failures; do not weaken a required check to make the slice look complete.
5. Return actual changed files, commands, outcomes, unresolved limitations and the resulting revision. Accept outputs against the contract before dependent work uses them.

[Anthropic's workflow guidance](https://www.anthropic.com/engineering/building-effective-agents) supports bounded composition and environmental feedback. [Current context documentation](https://code.claude.com/docs/en/memory) explicitly distinguishes instructions from enforced settings. **Adaptation:** build/test commands, package boundaries, generated files, legacy invariants, edit ownership and runtime tool access. **Failure evaluation:** two helpers changing the same interface must not silently overwrite one another; unrelated user edits must not be staged as part of the task.

## Test: assess behavior and the quality of the checks

**DM-P06 — assertion sensitivity; DM-P07 — integration realism.** DM05 highlights weak assertions and boundary data. DM09 describes a team policy requiring sandbox integration that the agent did not receive. Neither account justifies a global mutation threshold or prohibition on mocks. [DM05](https://harshasuraweera.medium.com/testing-the-testers-how-to-validate-ai-generated-automation-scripts-aff225b1baca), [DM09](https://scrolltest.medium.com/i-audited-my-own-test-suite-for-ai-generated-code-baac8a69fd13)

The verification skill should:

1. Derive required checks from accepted behavior and risk, then compare those checks with implementation coverage. Do not let the implementation alone define the expected answer.
2. Record dependency-realism policy: allowed mocks, maintained fakes, contract checks and required hermetic/real/sandbox integrations, each with a reason.
3. Inspect meaningful assertions and representative negative/boundary data. Where useful, confirm that a controlled defect or mutation causes the appropriate test to fail.
4. Run checks against an identified candidate and capture commands, environment, results and missing coverage. Distinguish pass, fail, not run and blocked.
5. Evaluate delivery-agent behavior separately from product behavior: scope preservation, evidence honesty, failed-check handling, authority compliance and handoff correctness.

The technical mechanisms are corroborated by [Stryker](https://stryker-mutator.io/docs/) and [Google's discussion of mock divergence](https://testing.googleblog.com/2013/05/testing-on-toilet-dont-overuse-mocks.html?hl=sk). Delivery-agent evaluation is grounded in [Anthropic's eval guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). **Adaptation:** critical journeys, test-double policy, environments, fixture data, time budgets and acceptable evidence gaps. **Failure evaluation:** an unavailable sandbox must produce an explicit limitation; replacing its required check with a convenient mock must not count as successful verification.

## Deploy: review intent, resource identity and actual authority

**DM-P08 — effective policy and authority; DM-P09 — deployment consequences; DM-P10 — operational signals.** DM04 offers governance questions. DM10 contributes an infrastructure migration experience where resource identity matters; DM06 contributes early instrumentation. These are inputs to a release procedure, not authorization to deploy. [DM04](https://pauldjohnston.medium.com/agentic-development-best-practices-0e23ab07c1f8), [DM10](https://medium.com/zar-engineering/building-an-ecs-golden-path-with-claude-code-and-aws-cdk-d4a580496801), [DM06](https://medium.com/lumigo/shifting-observability-left-in-the-sdlc-43ce83695a49)

The release skill should:

1. Bind the review to a candidate revision and artifact identity. Compare intent, specification, plan, diff and verification results; resolve material findings through the actual review policy.
2. Classify deployment effects: replacement/deletion, data migration, schema compatibility, access changes, operational dependencies and rollback limits.
3. Generate a deployment preview through the project adapter. Record its method, permissions, remote side effects and blind spots. Do not assume a command named “diff” or “dry run” is pure read-only execution.
4. Confirm existing action authority for the exact environment and candidate. If further approval is required, present the concrete candidate and evidence. Preserve established authorization instead of repeatedly requesting it.
5. Run only the authorized release path. Verify user-visible signals, rollback or containment conditions and the final environment state; capture outcomes even when the pipeline fails.

**Verified correction:** current `cdk diff` defaults to an automatic method that creates a CloudFormation change set using the deploy role and may fall back to a less precise template comparison. Its adapter must expose those facts. Changes to logical IDs can trigger resource replacement. [AWS diff reference](https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-diff.html), [AWS identifier guidance](https://docs.aws.amazon.com/cdk/v2/guide/identifiers.html)

The Medium article's echo-only hook is a warning, not an authorization block. Use the actual runtime decision semantics and enforce access outside prose. [Claude Code hooks](https://code.claude.com/docs/en/hooks) **Adaptation:** deploy adapter, environments, reviewers, identity-preservation rules, migrations, recovery strategy, signals and thresholds. **Failure evaluation:** an infrastructure refactor that replaces a stateful resource must not pass merely because unit tests and a warning hook succeeded.

## Maintain: investigate evidence, bound action and return learning

**DM-P11 — hypothesis-led diagnosis; DM-P12 — reviewed learning.** DM11 proposes alternative hypotheses and runbook retrieval. It is operational advice with vendor examples, not a measured incident study. Its suggestion to trust recurring model answers is not adopted. [DM11](https://medium.com/@nazarboyko/ai-for-debugging-production-issues-411bdb21fe8d)

The operations skill should:

1. Validate the authorized trigger, service, time window and observed symptom. Check signal freshness and whether the event is already being handled.
2. Fetch the minimum permitted evidence and applicable runbook revision. Treat logs, tickets and retrieved text as untrusted data; restrict sensitive-data exposure and expensive queries.
3. Separate observations from hypotheses. Attach corroborating and disconfirming checks; choose diagnostics by expected information, operational risk and cost.
4. Execute only a bounded action within existing authority and the actual runbook conditions. If the cause or authority is unresolved, preserve the investigation and escalate rather than inventing a remediation sequence.
5. Independently verify the resulting state and capture the incident timeline. Create linked follow-up intent for the accepted improvement; separately review proposals to change policy, runbooks, skills or regression tests.

[Google SRE's troubleshooting method](https://sre.google/sre-book/effective-troubleshooting/) supports evidence-based hypothesis testing. [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/) documents telemetry interfaces, not incident truth or automatic remediation authority. **Adaptation:** event source, deduplication, query budgets, data rules, service ownership, action allowlist, runbooks and recovery limits. **Failure evaluation:** a stale runbook or familiar symptom must not become a confirmed cause; missing current evidence must remain visible.

## Adoption decisions and rejected examples

These are implementation choices inferred from the evidence, with runtime behavior checked against primary documentation:

| Reusable part | Organization-specific part | Project/runtime-specific part |
| --- | --- | --- |
| Artifact/handoff contract and revision binding | Record authority and acceptance responsibilities | Tracker adapter, repository paths, revision lookup |
| Context manifest and source freshness check | Data access and retention policy | Package ownership, legacy constraints, tool versions |
| Verification result states and traceability | Risk criteria and required independent review | Commands, environments, dependency-realism policy |
| Action-scope and evidence checks | Who may authorize which consequential actions | Enforced permissions, sandbox, CI and deployment adapter |
| Incident hypothesis and follow-up contract | Escalation ownership and acceptable operational risk | Signals, runbooks, query limits, service recovery conditions |

Reject blanket staging of all changed files from DM12. Its custom command examples are not treated as current built-in CLI features. Reject consensus-as-proof from DM01/DM11, performance statistics from all articles, and comparison rankings from inaccessible DM07. Do not generalize a rigid restart/scale/config/rollback sequence from a sandbox example to arbitrary production systems.

Two additional discovery leads were opened but not promoted: [Jacob Wakeem's architecture-context article](https://medium.com/@jacob.wakeem/the-context-problem-in-ai-assisted-architecture-41acb83169d9) returned a fetch error, and [Ajay Ravichandran's Kubernetes ops article](https://medium.com/@ajay1105/what-happens-when-you-build-ops-agents-for-kubernetes-with-claude-code-0a89a4057c91) returned page chrome without an article body. Their search excerpts are not substituted for full reads.

This is a purposive sample. Product discovery and retirement remain less directly evidenced by Medium than implementation and testing. No article commands, third-party scripts or deployment examples were executed. The result is a set of traceable skill-design inputs and failure scenarios; implemented skills still need representative behavioral evaluation in the target runtime.
