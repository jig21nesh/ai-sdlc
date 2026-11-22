# 0001: Concise output contract

Status: accepted (22 November 2026)

## Context

Engineers reported that the artifacts the skills produce are too verbose to read and approve. Three causes were visible in the pack:

- The shared contract required about nine identity and provenance fields on every material output and seven items in every handoff.
- Templates used six- and seven-column tables and prose instructions that agents answered at length.
- No rule put the reviewer's decision first, and nothing capped questions or low-severity findings.

The recorded S01 exercise produced an 897-word specification and a 625-word plan for a small CSV export.

Published practice at Anthropic, Google and GitHub does not use word budgets for these documents. It uses fixed section lists, caps on questions and findings, severity ranking, collapsed reasoning and small changes. Anthropic's prompting guidance warns that hard per-sentence limits make prose choppy, and that telling a reviewer to report only severe issues reduces what it finds.

## Decision

Add one "Output rules" section to `skills/shared-contract.md` that every skill inherits:

1. Decision-first summary of at most five lines.
2. Fixed template sections, deleted when empty.
3. One line per requirement, task, check and finding; reasoning collapsed or linked.
4. Deviations in full; passes as a count with an evidence link.
5. Evidence linked, not pasted.
6. Inputs referenced by ID and revision, not restated.
7. At most three open questions, each with a recommended answer.
8. Findings ranked by severity; at most five low-severity items, with the withheld count stated; filtering happens after assessment.
9. Identity and provenance in one `Record` block at the end.
10. A routine artifact's body fits one page, about 400 words; a multi-component change may take three pages.
11. A failed check, unresolved decision, missing authorization or material risk is always stated.

Rewrite the intent, specification, plan, verification, release, incident and improvement templates to these rules, and point the nine core skills' return instructions at them. Plan and build aim for slices of about 100 changed lines and split near 1,000.

Do not set per-sentence or per-section word limits. The page target in rule 10 was added after the first rerun of S01 under rules 1 to 9: the outputs gained the decision-first summary and capped questions but grew, to 1,247 words for the specification and 1,115 for the plan. Structure alone did not shorten them. With the page target, a second rerun produced 960 and 770 words: about the same as before the change, and roughly twice the routine target. See the [rerun record](../../reviews/behavioral/S01-output-rules/REPORT.md).

## Consequences

- A reviewer can decide from the first screen of an artifact; detail remains available below it.
- The evidence the contract requires is unchanged. It moves to the `Record` block, a collapsed section or a linked file.
- Artifacts written from the earlier templates remain valid; nothing reads them by section name.
- The eleven specialist skills inherit the rules through the shared contract but keep their existing templates. They can be slimmed later if reviewers ask.
- Measured so far, the rules change where a reviewer looks first, not how much there is to read. Whether that answers the complaint is open, and enforcing the page target is the next lever.
- Caps can hide detail a reviewer wanted. The withheld count and the collapsed sections are the mitigation; the evaluate skill (ADR 0002) measures whether outputs become too thin.

## Sources

- [Anthropic AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook): five-part intent, review example capping nits at five.
- [Claude Code Review](https://code.claude.com/docs/en/code-review): severity table, collapsed reasoning.
- [GitHub Spec Kit](https://github.com/github/spec-kit): at most three clarification markers, delete unused sections, one line per task.
- [Kiro specs](https://kiro.dev/docs/specs/feature-specs/): one-line "WHEN … THE SYSTEM SHALL …" requirements.
- [Google engineering practices](https://google.github.io/eng-practices/review/developer/small-cls.html): about 100 lines is a reasonable change, 1,000 is usually too large.
- [Design docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/), a former engineer's account: a one-to-three-page document for incremental work.
- [Google SRE example postmortem](https://sre.google/sre-book/example-postmortem/): one-sentence summary, action items as a table, timeline last.
