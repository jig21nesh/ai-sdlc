# Validation after playbook reconciliation

Historical review of an earlier revision. See [deep-validation.md](deep-validation.md) for the current 20-skill pack and its evidence.

Reviewed 2026-10-08. This report supersedes the first implementation's terminology and candidate hashes; the earlier security/usability reports remain historical evidence of their original fixes.

## Source and content checks

Read the substantive [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook) and visually inspected its lifecycle and adoption diagrams. Added source O15 and official runtime references O16–O18. The register now has 35 sources. The [reconciliation](../research/playbook-reconciliation.md) separates source statements, source ambiguities and this toolkit's design decisions.

The reference diagram and its text alternatives now use the six source stage names. Twelve work modules remain as the toolkit's finer decomposition, with governance and retirement explicitly classified. Existing skill IDs and links are preserved. The mapping places initial discovery under Plan and implementation planning under Build. The delegation GIF is labeled an optional toolkit example and does not show dependent candidate verification running before a build exists.

All 15 skills were revised: twelve receive placement and completion-criterion clarification; orchestration, security and usability skills receive corresponding dependency, enforcement and source-checking refinements. The shared contract and templates identify authoritative records and separate software, delivery-agent and product-AI evaluation evidence. No agent runtime, hook, scheduled scan, permission expansion or external write was installed.

## Executed validation

- The official skill-creator `quick_validate.py` passed for all 15 skills using an existing temporary Python environment with PyYAML 6.0.3. No new package installation was needed. This checks skill structure, not runtime behavior.
- All 18 profile regression tests passed; example profiles still pass structure validation and deliberately fail readiness while decisions remain unresolved. No profile validator schema or executable permission setting was changed.
- JavaScript syntax and the existing control-logic tests passed. Source counts now come from data rather than assuming 31 records.
- The GIF generator validated three looping GIFs with four frames each, 1080×420 dimensions and static PNG equivalents. The revised lifecycle and delegation PNGs were visually inspected for clipping, labels and arrow meaning.
- The integrity checker now verifies the six source labels, complete/nonduplicated module classification and the distinction between initial and implementation planning, in addition to local links, assets and source mappings.
- An independent reviewer assessed the source/skill discrepancies and the revised candidate. See [playbook-skill-audit.md](playbook-skill-audit.md) for the final recheck and scenario scope.

## Remaining limits

This is a source reconciliation and local artifact review, not proof of production enforcement or a full accessibility assessment. Live browser, keyboard and screen-reader testing remains unperformed because the prior local-file browser policy and loopback-server sandbox restrictions remain applicable. No attempt was made to bypass them. Controller checks use a minimal DOM fixture, and diagram inspection does not verify the page's layout in a browser.

The source article's vendor examples, changing product availability and illustrative metrics are not treated as universal operational guarantees. Hook failures, permission modes, isolation, acceptance records and event-triggered actions require validation in the chosen runtime. Formal owner acceptance and authorization remain separate from this report.

## Final integration

The independent recheck addressed all seven conceptual findings and passed six content/manual scenarios. Final regeneration and local-link checks passed after updating the review status. No product-source change followed the recheck other than the generated status text. Final `index.html` SHA-256: `5badfabe1763c7ed573cd2e7389ba9554d067d13d12162e50d61b7ad2f98ed9b`.
