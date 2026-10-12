# AI-SDLC: research to implemented skills

Primary reference: [Anthropic's AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), reviewed 8 October 2026. The implementation is a portable **20-skill pack**, with explicit decisions, handoff templates and adaptation points. It is a set of agent instructions and reusable artifacts, not an installed execution service.

## What the analysis concludes

AI-assisted delivery needs more than code generation. The reusable unit is a bounded task with authoritative inputs, a meaningful behavioral check and evidence tied to the candidate. Organization-specific policy, project facts and runtime enforcement must remain separate. This is our engineering synthesis, informed by the sources below.

The primary model has six stages: **Plan, Design, Build, Test, Deploy, Maintain**. Initial problem capture and implementation planning are distinct. The [inventory](playbook-inventory.json) records **19 practices and sidebars**, including controls and artifact transitions. Its adoption prerequisites are not a mandatory order for every change. The existing twelve module IDs remain navigation aids; they do not replace the source taxonomy.

Three different dependencies need distinct treatment:

- Adoption: which capabilities make a practice useful or dependable.
- Artifacts: which accepted record/revision a particular decision uses.
- Execution: which tasks can run concurrently without unfinished dependencies or conflicting writes.

This distinction prevents a small documentation task from requiring complete corporate onboarding, while preventing a green checklist from authorizing a production action.

## What each evidence layer contributes

| Layer | Work performed | What it supports | What it does not establish |
| --- | --- | --- | --- |
| Primary | Full playbook practice inventory; selected linked runtime docs; Google/DORA/SRE and assurance references | Phase placement, operational patterns, current documented control semantics | Universal gains, automatic permission, correctness of every vendor example |
| GitHub | Seven repositories, 47 selected file observations at recorded SHAs, alongside the original repository catalog | Concrete contracts, tests, event/authentication paths, evaluation graders and failure cases | Upstream tests passing here, complete dependency/security audit, all code safely reusable |
| Medium | Twelve records; eleven accessible bodies and one partial discovery-only record | Practitioner failures and adaptation questions, checked against primary material | Benchmark rankings, representative performance, permission to copy commands into production |

The consolidated register contains **43 unique source URLs**: 18 primary records, 13 repositories and 12 Medium articles. Repeated URLs are enriched under stable IDs, with DG/DM aliases retained. Linked technical corroboration and inspected file URLs remain attached to their parent records and are not counted as independent endorsements. Start with [primary analysis](deep-primary-analysis.md), [GitHub file analysis](deep-github-analysis.md), [Medium analysis](deep-medium-analysis.md), and [all evidence](evidence.json).

## Implementation decisions

| Finding | Decision in this pack | Practical consequence |
| --- | --- | --- |
| A stage checklist does not tell an agent how to handle disagreement | Rewrite all 15 existing skills and add five distinct capabilities | Procedures name inputs, decision branches, output contracts and failure cases |
| Repository facts differ from reusable policy procedures | Separate repository-context and policy-skills | Stale command corrections do not become organization-wide policy |
| A hook callback or mode name does not prove denial | Guardrails tests actual effects and alternate/failure paths | A timeout or permission callback bypass cannot be reported as safe enforcement |
| A passing unit test may omit required real integration | Verification records test-double policy and missing environments | Required sandbox evidence stays unavailable, not silently replaced by mocks |
| Artifact validity differs from task correctness | Check record structure, then independently assess behavior and traces | A valid JSON report or existing file cannot certify the outcome |
| Aggregate eval scores can hide a forbidden action | Agent evals keep critical invariants separate and protect final holdouts | A high score cannot offset a disallowed delete or leaked secret |
| “Preview” can mutate remote state | Release records adapter method, side effects and preview limits | Commands such as CDK diff need scoped authority for their actual behavior |
| Agent agreement is not proof | Review uses reproducible evidence, including singleton findings | Majority voting cannot erase a concrete defect |
| Operations examples can assume a fixed remediation ladder | Operate separates diagnosis, authorized action and fresh verification | Similar symptoms do not automatically authorize restart, scaling or rollback |
| Triggered automation adds replay and credential risks | Canonical IDs, deduplication, exact target authority and runtime capability checks | Writing an intent or schedule proposal does not install an event handler |

All skill text and templates are original adaptations. No external repository code or article snippet is installed as an executor.

## Skills by phase

The [manifest](../skills/manifest.json) is the machine-readable source for paths, practice coverage, evidence and exact configuration fields. Every skill is stored locally under `skills/ai-sdlc-*/SKILL.md`.

| Phase | Skills and intended output |
| --- | --- |
| Plan | **discover**: evidence-bearing intent |
| Design | **specify**: combined behavior/design and acceptance matrix; **design**: material architecture decision |
| Build | **plan**: ordered repository-grounded implementation plan; **build**: patch and feedback evidence; **repository-context**: verified context changes; **policy-skills**: source-linked reusable policy procedure; **orchestrate**: dependency/ownership plan and integrated evidence |
| Test | **verify**: candidate-specific software proof; **agent-evals**: delivery-agent baseline/candidate comparison and invariant results |
| Deploy | **review**: findings or bounded comment repair; **release**: CI capability plan, preview/recovery evidence and authorized release record |
| Maintain | **operate**: event/incident diagnosis and follow-up; **security-scanning**: scan contract, triage and coverage; **improve**: measured intervention and regression results |
| Cross-cutting | **govern**: operating agreement; **guardrails**: action-control contract and conformance evidence; **security-review** and **usability-review**: independent findings |
| Additional lifecycle coverage | **retire**: transition, retained obligations and verified closure |

Retirement is supplemental coverage, not an invented seventh source stage. Security and usability can apply where warranted; they are not mandatory separate agents for every edit. PR review has review-only and repair branches. Release has CI preparation and execution branches. Channel intake is part of operations. These branches avoid multiplying shallow skills.

## Where and what an organization changes

1. **One task:** supply [TASK-BRIEF.md](../templates/TASK-BRIEF.md), the actual request and relevant repository instructions. Select needed skills; do not fill every optional profile field first.
2. **Organization rules:** version `config/org.local.json` or equivalent owned records for roles, data/model/tool boundaries, assurance, release authority and incident policy. The example is unresolved by design.
3. **Project facts:** version `config/project.local.json` or equivalent references for architecture, commands, acceptance, interfaces, integration realism, release mechanics and service operations.
4. **Runtime adapters:** implement and test tool scope, identity, credentials, artifact stores, event verification, scheduling, CI checks and approvals in the chosen host. Keep capability/side-effect evidence in the referenced adapter/control records. No universal vendor configuration can enforce all these boundaries.
5. **Core procedure:** change skill text only for demonstrated reusable gaps; retain concrete evidence and evaluate the changed skill against its prior version and near misses.

The manifest also lists suggested success signals per skill. Select measures with a baseline, denominator, observation window and owner; thresholds are local decisions. Pair throughput with quality, user impact and unauthorized-effect measures so faster work cannot hide failures. No vendor productivity numbers are adopted.

The detailed [adaptation guide](../config/ADAPTATION.md) and manifest name existing field paths rather than inventing a second incompatible schema. Null means unresolved; an empty allowlist grants no access. Existing authorization is reused within scope. Missing authority blocks the affected consequential action, while preparation continues.

## Coverage and validation

[Practice coverage](practice-coverage.md) connects every inventoried source item to implemented skills. [Validation](../reviews/deep-validation.md) distinguishes structural checks, actual local fixture exercises and unperformed live integrations. The purpose is traceable coverage of this primary reference, not a claim that a finite search found every AI-SDLC technique.

Still organization-specific: regulatory interpretation, actual risk acceptance, live permissions, provider terms, cost/latency targets, production incident exercises and proof of enforced boundaries. Browser layout and assistive-technology checks remain unverified in this environment. These limits do not prevent using the local skill procedures and templates.
