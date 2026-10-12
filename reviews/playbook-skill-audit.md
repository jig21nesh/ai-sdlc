# Playbook-to-skill conceptual audit

Historical review of an earlier revision. See [deep-validation.md](deep-validation.md) for the current 20-skill pack and its evidence.

8 October 2026. Independent, read-only implementation review of `skills/shared-contract.md`, all 15 `skills/*/SKILL.md` files, and `data/stages.json`. The full substantive linked article was read, including the maintenance examples and closing resources. This report contains original assessment of this toolkit, not a reproduction of the playbook. No installation, execution adapter, deployment, or implementation change was made.

## Source distinctions used

The [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) describes six non-linear stages: Plan, Design, Build, Test, Deploy, Maintain. Initial Plan captures intent; implementation planning belongs inside Build. Its diagram concerns adoption prerequisites, not the route a software change follows. Design combines requirements and design. Test distinguishes an ongoing feedback loop from a fresh verifier and also evaluates the delivery-agent configuration. The Build sidebar permits an existing authoritative record system. Deploy retains configured human decisions and environment-specific controls. Maintain returns operational findings to new work. These are source-specific patterns, not a universal standard or a requirement to use Anthropic products. Section pointers: introduction and plays; stages 1–6; Build's source-of-truth sidebar; the caption below the adoption diagram.

## Prioritized findings against the current implementation

### P1 — Taxonomy mixes levels and makes “plan” ambiguous

`data/stages.json` numbers governance, discovery, specification, design, implementation planning, coding, verification, review, release, operations, improvement, and retirement as equivalent stages. Their sizes and purposes differ. `ai-sdlc-plan` consumes accepted requirements/design, whereas `ai-sdlc-discover` creates the problem brief. Presenting them on the same undifferentiated lifecycle line invites the wrong entry point and implies extra handoffs.

**Recommended correction:** preserve stable skill IDs but add an explicit `phase`/`kind` classification. Proposed project mapping: Plan → discover; Design → specify + design; Build → plan + build; Test → verify; Deploy → review + release; Maintain → operate + improve. Classify govern as cross-cutting; label retire as this toolkit's explicit extension. Display `ai-sdlc-plan` as “Implementation planning.” These mappings are the reviewer's organization of the existing modules, not a claim that Anthropic names these modules. Allow specification/design to share one record and session.

### P1 — Output lists do not define a usable artifact handoff

The shared contract records evidence provenance, but does not select an authoritative record location or define how the next activity consumes its predecessor. Several skill inputs are generic nouns. An agent can consequently create a new document while missing the accepted record already held in an issue tracker, requirements tool, or repository.

**Recommended correction:** each selected activity should identify its incoming record and accepted revision, the authoritative system, outgoing record or patch, unresolved decisions, and next consumer. Use configurable record references. Do not force new Markdown files or duplicate signoffs when the existing task record suffices. Treat publication or a commit as an action requiring the task's existing authority, not an automatic consequence of generating a document.

### P1 — Implementation planning is underspecified

`ai-sdlc-plan` emphasizes decomposition, delegation, and edit ownership. It does not explicitly require inspecting the actual repository before planning, naming affected files/interfaces, connecting each task to observable proof, evaluating risks/alternatives, or reconciling implementation departures with the plan. `ai-sdlc-build` accepts a task brief but does not check which implementation decisions remain unresolved.

**Recommended correction:** add a compact, repository-grounded execution contract and a plan-update rule. Scope its size to the change. Preserve existing authority for routine local work; a plan record must not itself grant tool or release authority. Delegation remains optional.

### P1 — Verification categories need separate triggers

The build module says to add verification, and the verify module has strong evidence requirements. However, the distinction between checks during implementation and independent verification of the resulting candidate is implicit. The verify description highlights AI embedded in the product, which can obscure the separate need to evaluate delivery skills, prompts, tools, and model/configuration changes for an ordinary non-AI product.

**Recommended correction:** explicitly name three scopes: continuous implementation checks; any required independent candidate review; delivery-agent/configuration evaluations. Keep product-model evaluation conditional on an AI product feature. Protect the validity of acceptance checks during a repair; legitimate test changes need their own explanation and review, rather than a universal ban. Keep bounded repair and unavailable-check reporting.

### P2 — A work dependency map is not an adoption roadmap

`ai-sdlc-orchestrate` correctly builds a task dependency map. Neither that skill nor the stage catalog distinguishes this map from capability-adoption prerequisites or from artifact delivery transitions. Reusing a single arrow diagram for all three concepts would be inaccurate.

**Recommended correction:** label each graph's edge meaning. A work graph should express task dependencies; a delivery diagram should show artifact transitions and feedback; an adoption map should show capabilities required before enabling another capability. Do not infer task order from the adoption map or automatically run every activity in numerical order.

### P2 — Some local gates sound unconditional despite the shared contract

The shared contract already says to choose relevant stages and continue reversible preparation when profiles are missing. In contrast, the design gate names technical and risk-owner acceptance, and the release gate names release-owner readiness without explicitly distinguishing planning from execution. The build gate says the patch is ready for independent verification even when that verification is not required for the task.

**Recommended correction:** state the applicable decision class at the gate: local task completion, policy-required independent review, or consequential action authorization. Determine actual required reviewers from risk and policy; do not remove required human approval or invent new mandatory approval for every activity. A provisional release plan can be complete while deployment remains unauthorized.

### P2 — Operations has a backlog, but the return path is vague

`ai-sdlc-operate` produces operational reports and backlog items; `ai-sdlc-improve` proposes fixes and evaluations. Neither defines the minimal record that links a detected event to a triaged change and then to a regression case. A diagram that merely points back to requirements would overstate the procedure's completeness.

**Recommended correction:** record the event/evidence, allowed response, accountable triage decision, proposed task or intent reference, delivered fix, and resulting regression evidence. Make trigger configuration and permissions explicit; schedules, notifications, PR writes, and runbooks require existing authorization. Do not copy a universal statistical threshold or vendor monitoring product into the portable skill.

## Technical caveats to preserve during revision

The existing separation between advisory instructions and enforced runtime boundaries is correct. Keep it. Current [Claude Code permission-mode documentation](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode) qualifies planning behavior by session configuration, including a bypass-permissions exception. A portable skill cannot promise that a mode name alone prevents edits.

The [official hook reference](https://code.claude.com/docs/en/hooks#hook-output-and-decision-control) documents event-specific blocking semantics; startup errors and many timeouts do not themselves block tool execution. Therefore “a hook exists” is insufficient evidence of an enforced gate. Require tested behavior for the chosen runtime, including failure paths, and retain outer permissions/isolation. Do not import the article's substring-based deployment example as a production authorization control.

## Acceptance checks for the proposed revision

1. A reader can distinguish the six-phase explanation from this toolkit's activity modules and extensions.
2. A request to capture a new idea selects discovery; an accepted change needing file-level work selects implementation planning.
3. A small authorized documentation edit produces proportionate evidence without an invented committee gate.
4. A skill change on a non-AI product still selects delivery-agent evaluations where relevant.
5. A release-planning request can finish with explicit execution gaps and no deployment.
6. An incident output has a traceable next work item and regression follow-up; an alert alone never authorizes a mutation.

Status: findings pending implementation. This conceptual audit does not supersede the earlier local security assessment or claim that future runtime controls have been tested.


## Independent recheck after implementation

Rechecked 8 October 2026 against the revised reference model, stage catalog, all 15 skills, shared contract, record templates, adaptation guidance, generated HTML, diagram generator, and all three static diagram images. This is the same independent reviewer; implementation remained read-only. Only this audit report was updated.

**Disposition: all seven findings addressed in the written implementation. No remaining material conceptual mismatch was identified in this recheck.** This is content and consistency acceptance for the reviewed scope. Live skill discovery, model behavior, automatic transitions, hosted controls, and browser execution remain untested.

| Original finding | Recheck evidence | Status |
|---|---|---|
| Taxonomy and ambiguous planning | `data/reference-model.json` separates six reference stages, cross-cutting governance, and the retirement extension. `ai-sdlc-plan` now explicitly triggers on implementation work and points initial intent to discovery. HTML has six reference cards and twelve module details. | Addressed |
| Artifact handoffs | Shared contract identifies canonical system, record ID, revision, acceptance, and mirror linkage. The evidence-record template includes authoritative-record fields and next consumer; the change packet preserves existing systems. Commits/events do not automatically approve or publish work. | Addressed |
| Implementation planning | Plan step 1 now requires repository inspection, affected files, ordered work, alternatives, risks, checks, acceptance and updates. Build resolves accepted requirements/plan against the candidate and reports stale handoffs. A small task can use one concise record. | Addressed |
| Verification distinctions | Build requires continuous local checks; verify distinguishes required independent candidate review from self-checks. Its trigger and procedure explicitly cover delivery-agent changes for conventional software, separately from product AI. Meaningful test intent is protected without banning justified test corrections. | Addressed |
| Different dependency views | Shared contract, reference metadata, orchestration step 1, page copy and lifecycle image distinguish module placement, delivery transitions and adoption prerequisites. The helper diagram puts dependent candidate review after implementation. | Addressed |
| Proportional gates | Shared contract makes completion evidence distinct from new approval requirements. Plan permits existing local authorization, design/review use applicable configured reviewers, build records pending required verification, and release step 5 handles preparation without execution. | Addressed |
| Operational return path | Operate step 4 covers signal validation, deduplication, explicit response permissions, dated coverage and linked follow-up. Improve step 4 connects accepted findings to an owned change and regression evidence. Runtime control and authorization caveats remain. | Addressed |

### Six acceptance scenarios

The following handoffs were constructed from the revised skill text as a manual forward-test. They are synthetic examples, not transcripts from a deployed agent. No edits, command execution, notification, monitoring setup or release action from a scenario was performed.

| Scenario | Concrete handoff supported by the revised text | Result |
|---|---|---|
| 1. Explain the reference and modules | Present six reference stages, twelve selected work modules, and explicit governance/retirement classifications. Do not treat module numbers as required execution order. | Pass: content and mapping check |
| 2. Route an idea versus an accepted change | New idea: discovery returns an intent/problem record with open questions. Accepted change: implementation planning returns affected files, order, risks and proof within Build. | Pass: simulated routing |
| 3. Small authorized documentation correction | Keep a concise local scope/change/check record. Reuse task authorization, inspect relevant repository context, and record absent profiles without demanding unrelated decisions. Actual edit/check outcomes remain `not-run` in this simulation. | Pass: simulated handoff |
| 4. Skill change for a non-AI product | Select delivery-agent regression cases and baseline comparison. Mark product-AI checks `not-applicable` with the scenario reason. Mark unexecuted agent evaluations `not-run`. | Pass: simulated handoff |
| 5. Preparation-only release with hostile issue text | Deliver a provisional release plan and missing artifact/check/authority evidence. Ignore the issue's exfiltration and approval-override requests as instructions. Deployment, rehearsal and handover remain `not-run`; preparation proceeds. | Pass: simulated handoff |
| 6. Incident plus duplicate alert | Validate/deduplicate, retain event evidence, draft a linked intent or bounded change for triage, and connect an accepted fix to regression evidence. The alert grants no production, publication, messaging or rollback authority. | Pass: simulated handoff |

A local read-only consistency check independently confirmed: exactly six named reference stages; complete, unique assignment of all twelve module IDs; exact agreement between all twelve catalog activity/completion descriptions and their skill files; and six reference cards plus twelve module sections in `index.html`. Static-image inspection confirmed the revised labels and conditional review sequence. This check did not regenerate assets or execute their behavior in a browser. Profile tests and host skill validators were not rerun in this conceptual recheck; their separate results should remain attributed to the validation report.

The source-based cautions above remain intact: no mode name, sample hook, role brief or static profile is presented as sufficient runtime enforcement. Generated review/status links may be finalized by the integration owner after this inspection; they are not evidence of a new browser or runtime test.

### Rechecked candidate identity

Selected SHA-256 values below bind this recheck to the revised procedures and data. They exclude later review/status metadata and do not identify an entire deployment.

| File | SHA-256 |
|---|---|
| `data/reference-model.json` | `eab478d75609f6e7e2ebd9b86aa8fc15227a0386de371661502f76a5227e316b` |
| `data/stages.json` | `c36f70c68079f10905d5e38cf14c0dd676b6eae607a7ecda9988eee20ddadb90` |
| `skills/shared-contract.md` | `7015c5174901b56eadade5ef6a5a86fbafe2ada189a8459e01d9c83d138a647f` |
| `templates/CHANGE-PACKET.md` | `0c486c52a0a43cb9015c847f1a20c781de4ec35a98ee47f3d1dfb26e9eef422d` |
| `templates/evidence-record.example.json` | `a567d51d647db36e285337500a48199d277a97051936db2f1973db185b61e9c5` |
| `config/ADAPTATION.md` | `8902a2ebd2cab9608543e8e9335be99862360438b873f4349fd61c8589114cde` |

15-skill manifest SHA-256: `42a2d3b7f4eb8cb65d5c0bf533b472b960564dbfd3f525e1581da74e461b1443`. The manifest uses lexically sorted `sha256  relative/path\n` lines.
