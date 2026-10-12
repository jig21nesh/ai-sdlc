# Playbook reconciliation

Historical first-pass analysis. The comprehensive implementation and current evidence are in [SYNTHESIS.md](SYNTHESIS.md); retain this file for provenance.

The [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook), published 21 August 2026, was missing from the first source register. Its six stages differ from our earlier diagram. Our twelve items are now labeled **work modules**, with the mapping in [reference-model.json](../data/reference-model.json). Implementation planning belongs within Build; the initial Plan stage captures intent. Governance crosses the lifecycle; retirement is our additional coverage. The article's adoption graph is not a delivery sequence. Its Skills prose says no prerequisite, although its diagram draws an incoming context-file edge; that edge is not adopted as a mandatory dependency here.

## Corrections to this implementation

- Replaced the lifecycle GIF's labels and added a separate reference-to-module table. Other diagrams are explicitly labeled original toolkit designs.
- Retained existing skill paths so earlier links still work; clarified the planning skill's trigger and the module placement of every skill.
- Strengthened our evidence contract with authoritative-record identity, revision and accepted handoffs. Existing issue/requirements systems can remain authoritative.
- Updated our implementation/verification procedures to protect meaningful checks and evaluate the delivery agent even when the software product is not AI-based.
- Added explicit distinctions between isolated concurrent sessions, scoped helpers, continuous self-checking and independent final verification.
- Expanded operational procedures to cover authorized event intake, bounded response, dated scan results, incident follow-up and regression evidence.
- Kept our permission, review and release rules conditional on actual risk, policy and existing authority. No automatic approval, deployment or hook installation is added.

These procedural changes are the toolkit's engineering design. Additional technical references: [hook event semantics](https://code.claude.com/docs/en/hooks), [subagent isolation](https://code.claude.com/docs/en/sub-agents), [permission modes](https://code.claude.com/docs/en/permissions), and [agent evaluation methods](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). Vendor snippets, numerical examples and named beta products are not installed or generalized into universal requirements. The article's illustrative substring-based deployment hook is not a complete authorization mechanism.

## Verification scope

Read the article body and visually inspected its lifecycle and adoption diagrams. Rechecked official runtime documentation for the new technical guidance. See [the independent skill audit](../reviews/playbook-skill-audit.md) and [current validation](../reviews/playbook-validation.md) for findings, fixes and remaining limits. Historical review reports describe the first implementation and retain their original candidate hashes.
