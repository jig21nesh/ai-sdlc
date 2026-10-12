# Current bundle usability review

Reviewed at 2026-10-08T06:59:19.441432+00:00. Mode: static expert walkthrough plus safe local CLI execution, using `ai-sdlc-usability-review` and the shared contract. Overall evidence status: **partial**. No blocking task defect was observed in the inspected paths; one minor first-use documentation issue was corrected by the integration owner and rechecked statically. Owner acceptance is not supplied.

## Scope, audience and independence

Candidate: the 20 skill files, manifest/shared contract, README, task brief, HTML/CSS/JavaScript and organization/project adaptation/validator paths identified below. Assumed audience: a first-time engineer with an agent capable of reading local files; an enablement owner onboarding an organization; and a returning engineer choosing among adjacent skills. These are review assumptions, not recruited participants or research-derived personas.

No historical review reports, behavioral verdict manifest or unassigned fixture cases were inspected. The assigned E01, S01, U01 and C01 requests were executed separately from their raw inputs. Their artifacts are linked below. No preferred verdict was supplied.

This reviewer previously authored the plan/build/verify/release/operate skills, Medium research and original diagram assets. Accordingly, this is **not fully independent verification of those contributions**. The skill-selection assessment of the other 15 procedures and the static guide/CLI walkthrough are useful additional scrutiny, not a substitute for measured host routing or a representative-user study. No implementation edits were made during this review; only this report was written in the repository.

## Findings

### UX-01 — Minor, fixed: the skill-selection point lacked a concrete invocation example

- **Journey:** open the HTML index, choose a skill, and learn how to give it to an agent for a bounded task.
- **Location:** `scripts/build.py` skill-library section and generated `index.html#skills`.
- **Reproduction/method:** inspect the original HTML-first path. The skill library described portable instructions and linked skill files, but contained no explicit-path invocation example. The README had the concrete “Give your agent the selected … path” instruction. Both the sidebar and footer linked the README; a prior draft incorrectly called the sidebar link the sole link. The footer provides a recovery path. The supported gap was the absence of a concrete next action at the skill-selection point, requiring navigation elsewhere. This is static content inspection, **not** a measured user failure or live mobile result.
- **Expected:** the skill-selection point explains one concrete next action without requiring navigation elsewhere to learn how to apply a procedure.
- **Observed consequence:** a first-time reader had to infer how to apply the selected local file or navigate to the repository README. The likely extra friction is an expert inference; no measured user failure rate is claimed. The guide was still usable through its footer/desktop-sidebar links.
- **Correction:** add one short invocation example and a “Use the skills” README link in the skill-library section of the generator. Keep explicit-path use and task-relevant context distinct from optional host installation. Regenerate the index and statically confirm the new example/link is outside the hidden sidebar.
- **Disposition:** **fixed and statically rechecked** at 2026-10-08T06:59:58.717044+00:00. The integration owner added an explicit-path planning example, README usage link and short-brief link directly in `#skills`, then regenerated HTML. A parser confirmed the example and README link are inside `main > section#skills > .callout`, outside `.sidebar-bottom`, with no hidden ancestor. The mobile CSS does not hide that callout. The README heading and target skill exist. This closes the documented first-use issue; live narrow-screen behavior remains not-run. This reviewer did not implement the correction.

No second material defect was reproduced. Long policy documents and 91 unresolved readiness decisions are not themselves evidence that the simple-task path is blocked: that path explicitly permits the short brief and existing context. The readiness diagnostics are deliberately for reusable onboarding and are described accurately.

## Journey evidence

| Journey and observable success | Actual steps/method | Outcome and limits |
| --- | --- | --- |
| J1: a first-time contributor can select a bounded local documentation change without completing all profiles or acquiring production access | Read README “Use the skills” → short task brief → build description/shared contract; inspect relevant instruction and output paths | **Pass for documentation coherence.** Full profiles are explicitly optional for a small task, and existing authority is reused. No actual host invocation or routing was performed in this walkthrough. |
| J2: an HTML-first reader can select a skill and understand the next action | Inspect hero “Choose a skill” anchor, 20-row library, linked files and README entry point; inspect <=800px CSS | **Pass after static recheck.** Every skill is linked and the new in-section example/README link survives the relevant CSS visibility rule. No browser run. |
| J3: an organization owner knows where policy, project choices and runtime enforcement belong | README → `config/ADAPTATION.md` → example profiles → reviewed validator implementation → structure and readiness commands | **Pass for the exercised CLI/document contract.** Structure exit 0; readiness exit 1 with 91 named findings. No actual policies, references or runtime adapters verified. |
| J4: a returning engineer distinguishes adjacent procedures | Inspect all 20 frontmatter descriptions, phase/purpose manifest, shared boundaries and selected full procedures; apply the positive/near-miss matrix below | **Pass as a manual description assessment.** Does not measure automatic host selection, precision or recall. |
| J5: evidence and local resources remain discoverable | Parse HTML IDs/links and local Markdown references; simulate the shipped substring search over card attributes | **Pass for these static checks.** Zero duplicate HTML IDs, missing fragment targets or missing local targets; zero broken local links in the checked Markdown files. Search examples evaluation/privacy/retirement return 8/1/2 records; source aliases DM05/DG06 resolve. The invented unmatched term returns zero; markup provides recovery text. No external links opened. |
| J6: motion and accessibility have inspectable implementation support | Inspect image defaults, alt/caption text, controls, reduced-motion handling, landmarks, input labels, focus styles and table regions | **Partial.** Diagrams default to PNG; play/pause swaps GIF/PNG; reduced-motion changes stop playback; local links expose full-size diagrams; semantic controls and labeled scroll regions exist. No live animation, keyboard, zoom, mobile or assistive-technology journey was performed. |

## Manual skill-selection matrix

Each row is an expert reading of the actual description and boundaries, not a scored routing run. “Near miss” identifies adjacent work that should use the named alternative or remain within existing authorization.

| Procedure | Concrete positive request | Adjacent near miss / correct distinction |
| --- | --- | --- |
| govern | Prepare an owned pilot operating agreement | A local typo fix does not require new organization onboarding |
| discover | Turn an ambiguous support problem into intent | Implementation file sequencing belongs to plan |
| specify | Convert accepted intent into behavior/design and acceptance cases | A settled minor code correction need not restart discovery |
| design | Assess a material migration/resource identity choice | Routine edits do not require a separate architecture ceremony |
| plan | Inspect the repo and prepare implementation tasks for an accepted change | Initial product uncertainty belongs to discover; planning-only does not launch edits |
| build | Implement an authorized bounded correction with meaningful checks | A review-only request does not authorize repair |
| repository-context | Correct a stale package command in agent instructions | Reading context for an ordinary task need not rewrite it |
| policy-skills | Translate an identified owned policy into a reusable procedure | A third-party comment cannot invent policy or approve exceptions |
| guardrails | Inspect and test an actual runtime action boundary | A prompt/profile declaration is not enforcement |
| orchestrate | Coordinate dependencies and authorized separate work owners | A small single-owner change need not spawn agents |
| verify | Assess the actual software candidate against accepted behavior | Delivery-agent baseline comparison belongs to agent-evals |
| agent-evals | Compare skill/model/tool configurations on controlled tasks | Ordinary product tests alone do not evaluate delivery-agent behavior |
| review | Assess a candidate or repair supported review comments when requested | Assess-only does not imply editing, posting or merging |
| release | Prepare CI integration or a release for a bound artifact/environment | Preparation does not install CI, dispatch a job or deploy implicitly |
| operate | Diagnose an incident and execute only already authorized runbook steps | An incoming alert does not create unrestricted mutation authority |
| security-scanning | Prepare recurrence or triage dated scan results | Targeted independent security assessment is security-review; proposal is not scheduling |
| improve | Turn measured recurring mistakes into a tested intervention | One anecdote does not justify a universal new process gate |
| security-review | Assess a specific candidate's trust boundaries | Scan administration is security-scanning; no live exploit permission is created |
| usability-review | Walk real documentation/interface tasks with available tools | Generated personas or static descriptions are not observed users |
| retire | Plan retirement across consumers/jobs/credentials/data | One deleted deployment does not prove closure or authorize deletion |

The highest-confusion pairs are explicitly disambiguated: Plan/discover versus Build/plan; combined specify versus material design; verify versus agent-evals; security-review versus security-scanning; review-only versus repair; release preparation versus execution. Required source links and template paths resolved locally. Claims about automatic loading or tool restriction remain outside this manual assessment.

## Actual checks and related forward execution

- Python version: 3.14.5. `python3 -B scripts/validate_profiles.py --org config/org.example.json --project config/project.example.json` exited **0** and reported structure valid with unresolved nulls permitted. It also explicitly reported that references, permissions, approvals and certification were not verified.
- Adding `--ready` exited **1** with 91 field-specific findings, as the guide predicts; examples include `org.profile_id` and `project.quality.eval_suite_refs`. No configured command or adapter was executed. The validator source was inspected before execution.
- `node --check assets/app.js` exited **0**. This establishes syntax only.
- Local reference and static search checks above ran with Python standard-library parsers. No external content was fetched, no build/install was run and no historical review was used as evidence.
- Assigned forward exercise outputs: [E01 evaluation](behavioral/E01/REPORT.md), [S01 planning](behavioral/S01/REPORT.md), [U01 onboarding/scan/retirement](behavioral/U01/REPORT.md), [C01 repair](behavioral/C01/REPORT.md). The integrating agent updated these links to the archived copies shipped with the kit; original execution paths are recorded below.

Fixture reports are at `/private/tmp/ai-sdlc-forward-20261008/{E01,S01,U01,C01}/REPORT.md`. E01 did not promote from weak aggregate evidence or run a model; S01 produced provisional linked artifacts without code/delegation execution and disclosed plan authorship; U01 produced proposals without scheduling/contact/deletion; C01 reproduced a defect then passed three regression cases while declining an unsupported disclosure request. These are four specific manual agent executions, not evidence of universal skill effectiveness. E01/S01/U01 raw input hashes remained unchanged; all result JSON files parsed. C01's allowed source/test mutations have before/after hashes and saved unittest output.

## Remaining evidence and owner action

UX-01 is closed at the stated static level. A browser/device owner should subsequently exercise keyboard order, focus, search recovery, narrow table scrolling, zoom/reflow, GIF controls, reduced-motion behavior and assistive-technology announcements on the shipped guide. The host owner must test installation/discovery and actual selection with an unexposed suite if automatic routing will be relied upon. Representative contributors and organization owners should perform real adoption tasks before claiming measured usability.

Live browser, assistive technology, representative-user study, model-selection performance and runtime permissions are **not-run**. No browser bypass was attempted. No accessibility conformance, production readiness or complete independence is claimed. The absence of additional static findings is limited to these inspected candidates and tasks.

## Candidate identity after static remediation recheck

Initial UX-01 candidate: index SHA-256 `882acdd8e523b2d098f1a57b676195a42910620f1b9bf8c3450a2cfbd221676f`; generator SHA-256 `f155eb5c8ef5c1bcc9d0468691dab6c0177f730bdf8594dc5d6049b269d18a18`. The table below records the rechecked files. These hashes bind the report to observed files; concurrent integration changes require rechecking affected claims. They do not imply a Git commit, accepted revision or immutable packaged release.

| File | SHA-256 |
| --- | --- |
| `README.md` | `8f061e6f952f357e83cb6e72f05c83005781b6ed6451a3d78bef2a006dc3dca2` |
| `index.html` | `882acdd8e523b2d098f1a57b676195a42910620f1b9bf8c3450a2cfbd221676f` |
| `assets/app.js` | `c27e92f4e9eff755a5241a3fbffff432a90ea8cffe2778b6ce35c314313f1a08` |
| `assets/styles.css` | `1e94a2be33d211a44a24313bc3c8f8e33d3bc4c6dedc6e81e85f8aa19f2c4a57` |
| `config/ADAPTATION.md` | `cf2e529f16deb5f1e9db3ca9738d7d5ec5765e34e6cce81aa792eb00494fc8c3` |
| `config/org.example.json` | `fd9898267530c4add8e0abfb9aef41837300a3b6883e87ca17fd0cbd942777c1` |
| `config/project.example.json` | `cbc703bb2f5a07a350457324c211c2272b0ecf1c89cf1b0b0642986d78d0cfbe` |
| `scripts/validate_profiles.py` | `73fcb2e54a9d48114efd69dda939c1cbef3c4c0e177f913adaf27fffd5cb0d28` |
| `scripts/build.py` | `f2600dd182592d565edae263e91528c96cd9531dd23bd2c155f90632cc928c70` |
| `skills/shared-contract.md` | `05acac39cc690f0ccd067c637b7f0fde1cbc8fc5426676aae9b6429fb255ec08` |
| `skills/manifest.json` | `be1911479bf48806a684fc0758bd66056795a8889c42513c7c9ac324d6dd161f` |
| `templates/TASK-BRIEF.md` | `4687e24b899b5dd3364fbdbfd2d036aca15f368d86d56907600e09a3aa635a06` |
| `skills/ai-sdlc-agent-evals/SKILL.md` | `5b7c847b3656b97586a44ecc7742997fdda6cedf711a49a6ee4a41ee57032bac` |
| `skills/ai-sdlc-build/SKILL.md` | `ab4154d530bd3775399991bddc82b84f8c3a3a3ad2f48adc108f194f5074b504` |
| `skills/ai-sdlc-design/SKILL.md` | `c7e33676d400b3730c0e170ef2d49852ac38bf856d589da8fd5d6d1707221083` |
| `skills/ai-sdlc-discover/SKILL.md` | `f70bf8e9818881045e5233dc9ce069dee87e3dda824fa205f466b9022b805af2` |
| `skills/ai-sdlc-govern/SKILL.md` | `7c9fc37e5827210a766f5bee48d73b692d65fbaf2f42990e2341b2763cdf41d1` |
| `skills/ai-sdlc-guardrails/SKILL.md` | `455703bc59fbe72cdbf4a3d89b138116f8a02f9cd73eefc45156750700a1036c` |
| `skills/ai-sdlc-improve/SKILL.md` | `28a3dccd9f2843b7b4f79b69c379c3c4514af54b74ae0bff6a5630221ff00e76` |
| `skills/ai-sdlc-operate/SKILL.md` | `218306e1200f92698c47f2338f86558a599e1f25336286288557c5156ce51619` |
| `skills/ai-sdlc-orchestrate/SKILL.md` | `8b74dabe2a5e4deef44307cbc7162b2b1700efd44d74314e87ccc0d30e22a942` |
| `skills/ai-sdlc-plan/SKILL.md` | `e30d3a57e25ca89b8e876e63b69a623d16a363b7bc7c0e1e807d6a4c98078717` |
| `skills/ai-sdlc-policy-skills/SKILL.md` | `71eee139bd1953dc8580a24e4d13a980f32f06870b1d27216e9eb0117a97a2a6` |
| `skills/ai-sdlc-release/SKILL.md` | `490a68d7931372ce644827f2d418eb25e9a6a57f8b1ca633381af14f29ae8b37` |
| `skills/ai-sdlc-repository-context/SKILL.md` | `1e95b72726fb008ee8c734a6c81ba898a7104200e8e7d5684d31d64e8dce7c2e` |
| `skills/ai-sdlc-retire/SKILL.md` | `23f85da2d5e5efc1e3bdd3499f29dc828d2800869954823d0d07acd7cf0b20c0` |
| `skills/ai-sdlc-review/SKILL.md` | `00cf5d778f8b5899d4198da5ab7bc0640b2872b7104a57cebfe0326405a2f9d5` |
| `skills/ai-sdlc-security-review/SKILL.md` | `d0869050e83ef28d76e0ac1bd2b2fc1cad6e2c8047c879ca87697c2b42ebb926` |
| `skills/ai-sdlc-security-scanning/SKILL.md` | `023efffdd4d3048ffe5b67eae4e503bdf27d5f7baf9bed44eb1a9da4b7d9ba9b` |
| `skills/ai-sdlc-specify/SKILL.md` | `1a7854677e8888bf7693fb7bc77f940c43287550761107ca08699c5c2e33ede0` |
| `skills/ai-sdlc-usability-review/SKILL.md` | `e1f7215285c108c6cab0e16b3aeff969752189991e0aed243b51275c31d43f76` |
| `skills/ai-sdlc-verify/SKILL.md` | `8d6c48a770cb6a73c8ebbf7718e3e7a1e824177b0d5f0fcdf927304c19e5f35b` |

Integrating archival note: fixture report hyperlinks now resolve to preserved copies under `reviews/behavioral/`; original execution paths and candidate observations remain unchanged.
