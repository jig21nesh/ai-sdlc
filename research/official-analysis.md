# Primary-source analysis for a portable AI-assisted SDLC

Historical first-pass analysis. The comprehensive implementation and current evidence are in [SYNTHESIS.md](SYNTHESIS.md); retain this file for provenance.

Terminology note: stage IDs in this initial analysis refer to the toolkit's work modules. The current [reference mapping](../data/reference-model.json) and [playbook reconciliation](playbook-reconciliation.md) distinguish them from Anthropic's six stages.

Research date: 8 October 2026. The companion `official-sources.json` records the reviewed source, access level, concrete support, and limits. This is a curated evidence review, not a systematic literature review or a guarantee that all relevant research has been found. Stage names and proposed skill boundaries below are our synthesis; the publishers do not endorse this toolkit.

The scope is **using AI to develop and maintain software**. When the product itself contains an AI model or agent, add data, model, safety, and evaluation controls. An ordinary application developed with AI still needs requirements, architecture, testing, release, operations, and retirement practices.

## What the evidence changes

Improve the organization around the tooling. DORA's report overview treats AI as an amplifier of existing conditions. Its capabilities survey makes policy clarity, internal information quality, version control, small changes, user feedback, and platform usability visible adaptation targets. Measure delivery and user outcomes; generated lines of code are insufficient evidence of improvement. The survey is not causal proof. [O01](https://dora.dev/research/2025/dora-report/) · [O02](https://dora.dev/ai/capabilities-model/questions/)

Choose agent autonomy deliberately. Stable processes can use explicit workflows; uncertain tasks can use bounded agent loops. Parallel research and independent review are useful decomposition patterns, but delegation must include scope, inputs, outputs, and stop conditions. Model confidence is not verification. [O03](https://www.anthropic.com/engineering/building-effective-agents)

Package reusable procedures as skills and load supporting context when needed. A small entry point can reference stage-specific material, organization policy, and project evidence. The portable unit is the procedure and its contract, while the runtime supplies actual tool permissions. Inspect downloaded instructions and scripts before enabling them. [O04](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · [O05](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

Evaluate the entire system: model, prompt, tool definitions, memory, orchestration, and environment. Include repeated realistic tasks, regression cases, actual outcome checks, and human calibration of subjective grading. Keep production observations alongside offline results. [O06](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## Lifecycle coverage and proposed skill contracts

Every stage should identify required input, accountable owner, concrete output, acceptance evidence, and the next consumer. Missing evidence should remain visible as a gap. Re-entry and iteration are expected; this table is not a mandatory waterfall.

| Stage | Proposed skill responsibilities | Reviewable output | Evidence |
|---|---|---|---|
| Govern | Establish AI use boundaries, owners, risk tier, approved data/tools, exceptions | Organization profile and risk register | O02, O07, O08, O09 |
| Discover | Understand user needs, current system, constraints, and credible sources | Problem brief with assumptions and references | O01, O02, O04, O08 |
| Specify | Define acceptance criteria and security, privacy, reliability, accessibility requirements | Traceable requirements and acceptance examples | O06, O07, O08 |
| Design | Compare architectures, dependencies, trust boundaries, and operational tradeoffs | Decision record and threat model | O03, O07, O09, O11 |
| Plan | Split small tasks; assign ownership, dependency order, and release work | Bounded implementation plan with handoffs | O02, O03, O11 |
| Build | Implement scoped changes, manage dependencies, preserve context | Code, configuration, documentation, change evidence | O04, O05, O07, O10 |
| Verify | Check behavior, security, performance, accessibility, and agent regressions | Reproducible checks and unresolved failures | O06, O07, O09, O13 |
| Review | Independently inspect security, usability, design, tests, and evidence | Findings with scope, severity, disposition | O03, O09, O13 |
| Release | Package verified artifacts; establish authority, rollout, rollback | Release evidence and deployment plan | O10, O11 |
| Operate | Observe service/agent behavior; coordinate incident handling | Monitoring, runbooks, incident state, recovery evidence | O08, O09, O12 |
| Improve | Learn from user outcomes, delivery data, incidents, and evals | Prioritized improvement work and regression cases | O01, O02, O06, O14 |
| Retire | Plan safe transition and withdrawal; reconcile retained material | Approved decommission plan and completion evidence | O08, O13 |

Security belongs throughout development, including organizational preparation, component protection, secure production, and vulnerability response. SSDF deliberately supports risk-based adoption across technologies. [O07](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf)

Retirement is explicit: NIST GOVERN 1.7 concerns safe decommissioning, and MANAGE 4.1 connects operational monitoring to override, response, recovery, and phase-out. Our proposed retirement checklist should therefore include dependency migration, retention decisions, access revocation, and evidence of shutdown; those detailed checklist items are implementation choices requiring organization policy. [O08](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

## Organization and project adaptation

Keep a vendor-neutral core of stage contracts. Put organization owners, data classifications, tool/provider approvals, risk thresholds, retention rules, and escalation policies in a reviewed organization profile. Put repository layout, language, commands, architecture, test fixtures, service objectives, and environments in a project profile. Put concrete tool mappings and credential handling in runtime adapters. This separation is an architectural proposal informed by the sources, not a published universal standard.

Resolve profiles explicitly and record which versions apply to each run. Organization and project context should narrow the task and applicable permissions; retrieved pages, repository content, and sub-agent messages must not acquire authority to widen permissions. Tool-side checks should enforce resource scopes and any sensitive-action approvals. Security controls written only in Markdown are guidance, not an enforcement mechanism. [O09](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html)

Release adapters should record source revision, tested artifact, configuration, dependencies, and provenance, then apply the organization's release policy. Evidence of origin supports supply-chain integrity; it does not establish functional correctness. Rollout and rollback must fit the service's risk and operating environment. [O10](https://slsa.dev/spec/v1.2/) · [O11](https://sre.google/sre-book/release-engineering/)

Use agents to assist incident analysis within established command and remediation authority. Postmortems should lead to assigned fixes and reusable regression cases, with sensitive data removed from shared learning. [O12](https://sre.google/sre-book/managing-incidents/) · [O14](https://sre.google/sre-book/postmortem-culture/)

Review usability as experienced by a person performing the task: can they find the correct skill, understand required inputs, identify what is missing, inspect evidence, and recover from an error? Security and usability reviewers should report what they actually examined; neither an agent role title nor passing tests proves full coverage. [O13](https://google.github.io/eng-practices/review/reviewer/looking-for.html)

## Boundaries and refresh needs

No numerical productivity claim was extracted from the DORA report landing page. Anthropic material is first-party engineering guidance, not independent proof that its vendor or architecture is best. Historical Google SRE tools are examples, not requirements. NIST states that AI RMF 1.0 is being revised; the cited version must stay visible.

The [OWASP Agentic Applications 2026 landing page](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) was reviewed, but its PDF download returned HTTP 429. Detailed implementation guidance here instead uses the fully accessible OWASP AI Agent Security Cheat Sheet; no claim is made to have reviewed every Top 10 mitigation.

Future adoption requires checking organization-specific obligations, validating tool adapters in a sandbox, selecting representative tasks, and measuring outcomes against a baseline. A static guide and skill library can prepare that work; they cannot certify a live organization or runtime.
