---
name: ai-sdlc-improve
description: "Convert measured delivery outcomes, incidents and repeated agent mistakes into a scoped process, context, skill or evaluation improvement, with a baseline comparison and regression evidence."
---

# Improve from observed outcomes

Placement: **Maintain** with feedback across stages. Apply the [shared contract](../shared-contract.md). Improve the specific failure mechanism rather than accumulating permanent instructions for every anecdote.

## Procedure

1. Identify the observed failure or opportunity, affected revision/configuration and impact. Read actual artifacts, review findings and traces where authorized. Separate symptoms, hypotheses and verified contributing conditions; avoid blame or unsupported causal claims.
2. Establish a useful baseline: recurrence, escape/reopen rate, time waiting versus working, cost, reliability or user outcome. Include countermeasures to gaming (for example change failure alongside throughput). Describe sampling limits and confounders; anecdotal before/after changes do not establish causality.
3. Locate the smallest appropriate intervention:
   - Stale repository fact or command → repository-context.
   - Reusable judgment/policy application → policy-skills.
   - A hard constraint must hold before action → runtime guardrail, with a test.
   - Weak software proof → tests and verification.
   - Agent behavior regressed → delivery-agent eval and configuration.
   - Product/user problem → new intent; do not solve it by adding unrelated agent rules.
4. Define a hypothesis, expected observable improvement, unchanged behaviors to preserve and a revisit/rollback condition. Select one bounded change or explain coupled changes. Preserve the failing case in sanitized form without copying private logs into prompts.
5. Implement the authorized intervention. For skill/context/hook/model/tool changes, use agent evaluation with a prior-version or no-skill baseline as appropriate, realistic tasks, near misses and unexposed final cases. Match budgets and environments; retain actual outputs and trace evidence.
6. Check for displaced costs, over-triggering, newly blocked ordinary work and privacy/permission regressions. Compare evidence to the hypothesis; retain, revise or revert based on results. Treat an inconclusive result as inconclusive.
7. Update relevant knowledge, tests and owners with links to evidence. Record follow-up ownership; do not create schedules or contact teams solely because a follow-up would be useful.

## Output and completion

Use [improvement-record.md](assets/improvement-record.md). Return observation, diagnosis confidence, intervention location, baseline/candidate comparison, residual gaps and actual adoption decision. Completion requires evidence supporting the claimed improvement or an honest inconclusive/rejected result, not merely a new rule.

**Failure case:** a single missed instruction leads to a blanket “always run every test” rule. First determine whether discovery, stale context, an unavailable tool or insufficient verification caused the miss; test the smallest correction against ordinary tasks.

## Adaptation

Use `project.quality.eval_suite_refs`, `org.ai.evaluation_policy_ref`, `project.context.instructions_paths`, `org.assurance.required_checks` and the applicable policy/skill repository. Product metrics live in `project.product.success_metrics`; service outcomes in `project.operations.slo_ref`. Thresholds and adoption authority are local decisions.

## Basis

[Google SRE postmortem culture](https://sre.google/sre-book/postmortem-culture/) supports learning from incidents. [Anthropic agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) supports outcome/trace evaluation. [Deep GitHub research](../../research/deep-github-analysis.md) provides concrete skill-comparison patterns and held-out-set caveats.
