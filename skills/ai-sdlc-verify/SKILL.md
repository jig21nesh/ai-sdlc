---
name: ai-sdlc-verify
description: "Verify a specific software candidate against accepted behavior and risk, assess whether its tests are meaningful, and separate software evidence from delivery-agent and product-AI evaluations."
---

# Verify the candidate, not its claims

This **Test** procedure establishes what was actually checked for a particular candidate.
Read the [shared contract](../shared-contract.md) for evidence statuses, authority and repair limits.
The verification report can be complete while the candidate still has failed or unavailable required checks.
Do not label that candidate fully passed or infer risk acceptance from report completion.

## Select evidence scopes

Resolve accepted intent/specification, implementation plan, patch, prior failures and the candidate revision/digest.
Load the actual [org](../../config/org.example.json) and [project](../../config/project.example.json) profiles through their designated locations.

- `org.assurance.required_checks`, `independent_review_required`, `security_review_risk_tiers`, `usability_review_required`: mandatory review/check scope.
- `org.ai.evaluation_policy_ref`, `project.quality.eval_suite_refs`: delivery-agent evaluation policy and suites.
- `project.quality.acceptance_ref`, `required_checks`, `performance_budgets_ref`: intended behavior and measurable expectations.
- `project.quality.security_verification_ref`, `accessibility_verification_ref`: specialist verification contracts.
- `project.risk.contains_ai_product_features`, `threats_ref`: conditional product-AI scope and threat cases.
- `project.workflow.review_policy_ref`: independent reviewer requirements and defect/exception policy.
- `project.commands`, `org.tools`, `org.data`: inspected check definitions, execution limits and permitted test data.

Distinguish these scopes before running tools:

| Scope | Evaluate when | Evidence |
| --- | --- | --- |
| Software candidate | Its behavior or quality is in scope | Tests, analysis, behavior observations and requirement traceability. |
| Delivery agent | Model, skill, instructions, hooks or tools change materially; or policy requires a regression | Task outcomes, execution traces, scope/authority behavior, costs and limits. |
| AI inside the product | The product includes relevant model behavior | Held-out domain cases, safety/quality metrics and appropriate human assessment. |

Conventional software still needs delivery-agent evaluation when its automation changes.
A product without AI does not need fabricated product-model metrics.

## Build the verification matrix

1. Map each affected requirement, interface and material threat to an appropriate check.
2. Derive expected outcomes from accepted behavior, not solely from the new implementation.
3. Include representative failure, boundary, authorization, recovery and accessibility paths where relevant.
4. Identify existing checks, necessary additions, environment/data requirements and evidence gaps.
5. Separate deterministic checks from model judgments and human decisions; record which one each claim relies on.
6. Choose a proportionate suite. A small reversible edit need not acquire an unrelated exhaustive test program.

Use [the verification-report template](assets/verification-report.md) when a durable matrix is useful.
Store it in `project.context.artifact_dir` or the existing authoritative verification system.
A statement such as “tested the API” is insufficient: identify behavior, target revision, environment and result.

## Inspect the tests as well as the product

Read critical generated assertions and fixtures before trusting a green result.
Check that assertions would detect the relevant wrong result and that negative test data is actually invalid.
Review mocks/fakes against the policy referenced by `project.quality.acceptance_ref` and `project.workflow.review_policy_ref`.
Record why a dependency is mocked, faked, tested by contract, hermetically exercised or checked in an approved sandbox.
If that policy is absent, propose a risk-based choice; do not invent a universal ban on mocks.
If a required integration cannot run, retain the gap. A mock is not equivalent evidence merely because it passes.
Use targeted mutation or deliberate defect injection when it materially tests sensitivity and is safe in an isolated candidate.
Restore the candidate after such experiments and verify that only intended changes remain.
Do not impose an arbitrary mutation/coverage percentage or treat either metric as correctness proof.

## Run and assess checks

1. Confirm the command's actual side effects, credentials, network use, hooks and time limits.
2. Run the reviewed check against the identified candidate in the authorized environment.
3. Capture start/end time, command/tool version, candidate identity, exit status and relevant redacted output.
4. Compare the result with the expected behavior; inspect scanner findings for applicability and evidence.
5. Record a failure as observed. Distinguish product defects, broken tests, baseline failures and environment faults with support.
6. After a repair, bind results to the new candidate and rerun affected checks. Broaden only when new risk or failure warrants it.

An exit code alone may be insufficient when a runner skipped tests, reported zero cases or ignored a failed subprocess.
A timed-out, skipped or unavailable check must not inherit the last successful result from another revision.
Do not alter acceptance criteria or disable checks during verification to manufacture success.
Correcting a demonstrably wrong check requires evidence and the review appropriate to the task.

## Obtain independent evidence where required

Give the verifier accepted requirements, candidate identity, environment instructions and necessary context.
Keep expected behavior available; avoid supplying a desired verdict or relying only on the builder's narrative.
Independent context is useful but not equivalent to independent permissions or a different failure mode.
Have the reviewer inspect the actual patch/artifact and report evidence, severity, affected behavior and residual uncertainty.
Resolve contradictory findings using reproduction or source evidence; majority agreement is not a proof rule.
If no independent verifier is available, record that requirement as unmet rather than accepting the producer's self-review.

## Evaluate the automation when in scope

Use the suite selected by `project.quality.eval_suite_refs` and `org.ai.evaluation_policy_ref`.
Include representative tasks and negative cases such as injected issue instructions, stale handoffs and unavailable tools.
Assess actual outcomes and permitted side effects, not merely whether a response mentions the right words.
Use held-out cases, repeated trials when variability matters, calibrated model graders and human judgment where needed.
Record model/tool/skill versions, candidate configuration, task budget, cost and baseline comparison.
Report data leakage, uncalibrated graders or missing runs as limitations.
For substantial evaluation work, use the agent-evaluation procedure available in the bundle; do not invent results if its runner is unavailable.

## Return an honest verdict

List each check as `pass`, `fail`, `partial`, `blocked`, `not-run` or `not-applicable` with a reason and evidence link.
Separate requirement coverage, software defects, agent behavior findings and product-AI results.
Name untested critical behavior and the impact of environment/independence limits.
Route residual-risk acceptance to the actual quality/domain owner under the review policy; the verifier does not self-authorize a release.
State what changed after repairs and which final-candidate checks were rerun.

Cases to distinguish: a passing mock with a missing required integration; zero discovered tests with exit 0; a fluent AI judgment without reproduction; and a new patch accompanied by old CI evidence.

Basis: [Anthropic eval methods](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [Google review guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html), [Stryker mutation testing](https://stryker-mutator.io/docs/).
Practitioner pitfalls: [DM-P06 and DM-P07](../../research/deep-medium-analysis.md), corroborated by [Google on mock divergence](https://testing.googleblog.com/2013/05/testing-on-toilet-dont-overuse-mocks.html?hl=sk).
