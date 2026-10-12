# Source-practice implementation coverage

Generated from the inventoried source practices and skill manifest. The capability descriptions are this toolkit’s synthesis. Typed source dependencies remain in [playbook-inventory.json](playbook-inventory.json); they are not a mandatory execution sequence.

| Practice ID | Source phase / pointer | Implemented skills |
| --- | --- | --- |
| intent | Plan / Stage 1 / intent entry | [ai-sdlc-discover](../skills/ai-sdlc-discover/SKILL.md) |
| spec-design | Design / Stage 2 / specification work | [ai-sdlc-specify](../skills/ai-sdlc-specify/SKILL.md), [ai-sdlc-design](../skills/ai-sdlc-design/SKILL.md), [ai-sdlc-usability-review](../skills/ai-sdlc-usability-review/SKILL.md) |
| implementation-plan | Build / Stage 3 / implementation planning | [ai-sdlc-plan](../skills/ai-sdlc-plan/SKILL.md), [ai-sdlc-build](../skills/ai-sdlc-build/SKILL.md) |
| autonomy | Build / Stage 3 / autonomous-mode sidebar | [ai-sdlc-guardrails](../skills/ai-sdlc-guardrails/SKILL.md) |
| canonical-records | Cross-cutting / Stage 3 / record-system sidebar | [ai-sdlc-govern](../skills/ai-sdlc-govern/SKILL.md) |
| repo-context | Build / Stage 3 / repository instructions | [ai-sdlc-repository-context](../skills/ai-sdlc-repository-context/SKILL.md), [ai-sdlc-improve](../skills/ai-sdlc-improve/SKILL.md) |
| policy-skills | Build / Stage 3 / reusable policy procedures | [ai-sdlc-policy-skills](../skills/ai-sdlc-policy-skills/SKILL.md), [ai-sdlc-improve](../skills/ai-sdlc-improve/SKILL.md) |
| build-hooks | Build / Stage 3 / build controls | [ai-sdlc-guardrails](../skills/ai-sdlc-guardrails/SKILL.md), [ai-sdlc-security-review](../skills/ai-sdlc-security-review/SKILL.md) |
| sessions-helpers | Build / Stage 3 / concurrency | [ai-sdlc-orchestrate](../skills/ai-sdlc-orchestrate/SKILL.md) |
| feedback-tests | Test / Stage 4 / implementation feedback | [ai-sdlc-build](../skills/ai-sdlc-build/SKILL.md), [ai-sdlc-verify](../skills/ai-sdlc-verify/SKILL.md) |
| agent-evals | Test / Stage 4 / delivery-agent evaluation | [ai-sdlc-agent-evals](../skills/ai-sdlc-agent-evals/SKILL.md), [ai-sdlc-improve](../skills/ai-sdlc-improve/SKILL.md) |
| pr-review | Deploy / Stage 5 / review in both directions | [ai-sdlc-review](../skills/ai-sdlc-review/SKILL.md), [ai-sdlc-usability-review](../skills/ai-sdlc-usability-review/SKILL.md) |
| approval-hooks | Deploy / Stage 5 / action approval controls | [ai-sdlc-guardrails](../skills/ai-sdlc-guardrails/SKILL.md), [ai-sdlc-release](../skills/ai-sdlc-release/SKILL.md), [ai-sdlc-security-review](../skills/ai-sdlc-security-review/SKILL.md) |
| ci-delivery | Deploy / Stage 5 / pipeline integration | [ai-sdlc-release](../skills/ai-sdlc-release/SKILL.md) |
| trigger-intake | Maintain / Stage 6 / event-to-work loop | [ai-sdlc-operate](../skills/ai-sdlc-operate/SKILL.md), [ai-sdlc-improve](../skills/ai-sdlc-improve/SKILL.md) |
| recurring-scans | Maintain / Stage 6 / scheduled security assessment | [ai-sdlc-security-scanning](../skills/ai-sdlc-security-scanning/SKILL.md), [ai-sdlc-security-review](../skills/ai-sdlc-security-review/SKILL.md) |
| channel-intake | Maintain / Stage 6 / channel-driven on-call | [ai-sdlc-operate](../skills/ai-sdlc-operate/SKILL.md) |
| managed-controls | Cross-cutting / Stage 5 / managed enterprise example | [ai-sdlc-govern](../skills/ai-sdlc-govern/SKILL.md), [ai-sdlc-guardrails](../skills/ai-sdlc-guardrails/SKILL.md), [ai-sdlc-security-review](../skills/ai-sdlc-security-review/SKILL.md) |
| artifact-transitions | Cross-cutting / Introduction / artifact transitions | [ai-sdlc-govern](../skills/ai-sdlc-govern/SKILL.md), [ai-sdlc-discover](../skills/ai-sdlc-discover/SKILL.md), [ai-sdlc-specify](../skills/ai-sdlc-specify/SKILL.md), [ai-sdlc-plan](../skills/ai-sdlc-plan/SKILL.md), [ai-sdlc-build](../skills/ai-sdlc-build/SKILL.md), [ai-sdlc-orchestrate](../skills/ai-sdlc-orchestrate/SKILL.md), [ai-sdlc-verify](../skills/ai-sdlc-verify/SKILL.md), [ai-sdlc-review](../skills/ai-sdlc-review/SKILL.md), [ai-sdlc-release](../skills/ai-sdlc-release/SKILL.md), [ai-sdlc-operate](../skills/ai-sdlc-operate/SKILL.md) |

All 19 inventoried items have an implementation entry point. This is coverage of named practices, not proof of correct runtime execution. See [validation](../reviews/deep-validation.md) for observed results and limits.
