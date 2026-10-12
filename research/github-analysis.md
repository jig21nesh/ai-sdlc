# GitHub evidence: reusable AI-SDLC patterns

Historical first-pass analysis. The comprehensive implementation and current evidence are in [SYNTHESIS.md](SYNTHESIS.md); retain this file for provenance.

Terminology note: stage IDs in this initial analysis refer to the toolkit's work modules. The current [reference mapping](../data/reference-model.json) and [playbook reconciliation](playbook-reconciliation.md) distinguish them from Anthropic's six stages.

Researched 2026-10-08. This is a curated implementation-oriented sample, not an exhaustive inventory or endorsement. Ten primary repositories were opened; README contents and the selected files below were inspected. No third-party code was cloned, installed or run. `access: full` means the cited public README was accessible, not that every repository file was audited. Publication dates are null because the records represent evolving repositories. Default-branch links are mutable; pin a reviewed commit or release before adoption. Security, ongoing maintenance and transitive licenses have not been independently audited.

## What the sources establish

| Evidence | Reusable concept | Inspected files / evidence |
| --- | --- | --- |
| G01 · Spec Kit | Durable specifications and explicit workflow artifacts; project conventions can be adapted separately from added capabilities. | [README](https://github.com/github/spec-kit/blob/main/README.md), [customization guide](https://github.com/github/spec-kit/blob/main/docs/guides/customization.md), [persistence models](https://github.com/github/spec-kit/blob/main/docs/concepts/spec-persistence.md) |
| G02 · Anthropic Skills | Package specialized procedures in small folders; describe invocation intent clearly. | [README](https://github.com/anthropics/skills/blob/main/README.md), [template](https://github.com/anthropics/skills/blob/main/template/SKILL.md) |
| G03 · Google ADK | Model orchestration as inspectable code and evaluate tool behavior as well as final text. | [README](https://github.com/google/adk-python/blob/main/README.md), [evaluation configuration](https://github.com/google/adk-python/blob/main/contributing/samples/evaluation/basic_criteria/eval_config.json) |
| G04 · LangGraph | Make workflow state, interrupts, retries and recovery explicit. | [README](https://github.com/langchain-ai/langgraph/blob/main/README.md), [types and policy definitions](https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/langgraph/types.py), [license](https://github.com/langchain-ai/langgraph/blob/main/LICENSE) |
| G05 · Promptfoo | Separate prompts, models, test cases and assertions so regressions can be compared. | [README](https://github.com/promptfoo/promptfoo/blob/main/README.md), [example configuration](https://github.com/promptfoo/promptfoo/blob/main/examples/getting-started/promptfooconfig.yaml), [configuration guide](https://github.com/promptfoo/promptfoo/blob/main/site/docs/configuration/guide.md) |
| G06 · Scorecard | Check concrete repository and dependency controls, keeping heuristic findings distinct from guarantees. | [README](https://github.com/ossf/scorecard/blob/main/README.md), [check definitions](https://github.com/ossf/scorecard/blob/main/docs/checks.md) |
| G07 · SLSA | Keep verifiable artifact provenance and select explicit supply-chain requirements. | [README](https://github.com/slsa-framework/slsa/blob/main/README.md), [v1.2 build track](https://github.com/slsa-framework/slsa/blob/releases/v1.2/spec/build-track-basics.md), [verification guidance on main](https://github.com/slsa-framework/slsa/blob/main/spec/verifying-artifacts.md) |
| G08 · OpenTelemetry | Keep operational instrumentation portable across implementations and destinations. | [README](https://github.com/open-telemetry/opentelemetry-specification/blob/main/README.md), [architecture overview](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md) |
| G09 · ACP | Isolate editor/agent integration and negotiate capabilities instead of assuming interchangeability. | [README](https://github.com/agentclientprotocol/agent-client-protocol/blob/main/README.md) |
| G10 · AGENTS.md | Put project-specific setup, verification commands and contribution conventions in a predictable file. | [README](https://github.com/agentsmd/agents.md/blob/main/README.md), [license](https://github.com/agentsmd/agents.md/blob/main/LICENSE) |

## Stage coverage and proposed skills

The following is this project's synthesis, not a claim that any source prescribes the complete lifecycle. Skills are reusable procedures; the tool named in an adapter is replaceable. A stage may loop back when evidence fails its acceptance criteria.

| Stage | Proposed skills | Required artifact / handoff | Relevant evidence |
| --- | --- | --- | --- |
| Govern | Policy intake; data classification; tool approval; dependency intake | Versioned organization constraints, owners and exceptions | G01, G02, G06, G10 |
| Discover | User research; repository reconnaissance; idea assessment | Evidence-backed problem statement, assumptions and go/stop decision | G01 |
| Specify | Requirements; acceptance criteria; nonfunctional requirements; traceability | Testable specification linked to evidence | G01 |
| Design | Architecture alternatives; threat modeling; accessibility design; integration contracts | ADRs, trust boundaries and interface contracts | G03, G06, G08, G09; threat-model specifics require additional security sources |
| Plan | Work decomposition; dependency ordering; risk sizing; bounded delegation | Tasks with owners, entry criteria, outputs and budgets | G01, G03, G04, G10 |
| Build | Scoped implementation; dependency selection; agent/skill authoring | Reviewable change plus updated design and test artifacts | G02, G03, G04, G06, G10 |
| Verify | Functional tests; model evaluations; adversarial tests; performance and accessibility checks | Results with versions, failed cases and unresolved gaps | G03, G05, G06; accessibility standards need separate evidence |
| Review | Independent security review; usability review; human change review | Findings, fixes, residual risks and required approvals | G06; reviewer workflows here are design recommendations |
| Release | Artifact provenance; rollout planning; rollback rehearsal | Immutable artifact identity, provenance, deployment and rollback evidence | G05, G07 |
| Operate | Trace analysis; incident response; reliability monitoring | Operational telemetry, incidents and remediation decisions | G04, G08 |
| Improve | Failure analysis; regression corpus maintenance; skill evaluation | Measured changes and versioned skill/model comparison | G01, G05, G08 |
| Retire | Dependency/service inventory; access revocation; retention and deletion planning | Approved shutdown plan, consumer migration and closure record | Coverage gap: these repos do not establish a complete retirement process |

## Organization and project separation

Recommended layering is a design inference from these sources. It should be enforced by the host/runtime and CI where enforcement matters; Markdown alone cannot enforce policy.

| Layer | Put here | Change when |
| --- | --- | --- |
| Core skill contract | Inputs, procedure, outputs, evidence, failure behavior | The reusable method changes |
| Organization profile | Risk tiers, data handling, permitted providers, approval roles, evidence retention | Adopting a new organization or changing policy |
| Project profile | Build/test commands, architecture, repository paths, dependencies, service owners and SLOs | Adopting a new project or changing its implementation |
| Tool adapter | Provider/model selection, tracker/SCM/CI mappings, supported capabilities | Replacing a vendor or tool |
| Task record | Scope, acceptance tests, execution identity, artifact versions and review decisions | Every unit of work |

Keep non-negotiable organization constraints from being silently weakened by a project override. Detect conflicts, explain them and route policy exceptions to an accountable owner. Test the effective configuration. Store credentials in the organization's secret system, with references in profiles rather than secret values. These are proposed controls; none of these repositories makes an arbitrary custom layering scheme secure automatically.

## Overlap and adoption cautions

- Spec Kit and AGENTS.md overlap in project guidance. Use one canonical owner for each rule and link it from the other surface instead of maintaining contradictory copies.
- Anthropic Skills packages procedures; ADK and LangGraph execute agent workflows. A skill is not a replacement for runtime authorization. Choose orchestration infrastructure for an actual need rather than adopting both by default.
- ADK evaluations and Promptfoo overlap in regression testing. Keep a common evaluation dataset and explicit model/provider versions; use trajectory checks when tool behavior matters. Sample thresholds are examples, not organization policy.
- Scorecard, security testing and SLSA address different risks. AI review does not satisfy Scorecard's human Code-Review criterion. Provenance does not prove application correctness, and a high repository score does not prove safety.
- OpenTelemetry and framework tracing can overlap. Define one evidence schema, redact at every export boundary and test what child operations emit. LangGraph's node TracePolicy explicitly warns it is not complete secret redaction.
- ACP covers editor/agent communication. It does not standardize the whole SDLC, organization permissions or all agent-to-agent exchanges.
- Anthropic's repository has mixed licenses. Do not bulk-copy all skills on the assumption that every directory is Apache-2.0. Inspect the specific files and license terms needed.

Remaining evidence gaps are organizational decision rights, sector-specific obligations, user-research methods, accessibility standards, incident policy and retirement/data-erasure requirements. Fill those from the organization's authoritative sources; do not present this GitHub sample as complete coverage.
