# 0001: Concise output contract

Status: accepted (22 November 2026)

## Context

An artifact that a person must approve should show its decision on the first screen. The pack's outputs did not, for three reasons:

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

Do not set per-sentence or per-section word limits. Rule 10 gives a target for the whole artifact because structure rules alone do not shorten output: in the [S01 rerun](../../reviews/behavioral/S01-output-rules/REPORT.md), rules 1 to 9 without a size target produced longer artifacts than the earlier templates.

## Consequences

- A reviewer can decide from the first screen of an artifact; detail remains available below it.
- The evidence the contract requires is unchanged. It moves to the `Record` block, a collapsed section or a linked file.
- Artifacts written from the earlier templates remain valid; nothing reads them by section name.
- The eleven specialist skills inherit the rules through the shared contract but keep their existing templates. They can be slimmed in the same way.
- In the S01 rerun the rules changed where a reviewer looks first more than how much there is to read: with the page target, the specification and plan were about as long as before and roughly twice the routine target. Enforcing the target through the evaluate skill is the next lever.
- Caps can hide detail a reviewer wanted. The withheld count and the collapsed sections are the mitigation; the evaluate skill (ADR 0002) measures whether outputs become too thin.

## Sources

- [Anthropic AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook): five-part intent, review example capping nits at five.
- [Claude Code Review](https://code.claude.com/docs/en/code-review): severity table, collapsed reasoning.
- [GitHub Spec Kit](https://github.com/github/spec-kit): at most three clarification markers, delete unused sections, one line per task.
- [Kiro specs](https://kiro.dev/docs/specs/feature-specs/): one-line "WHEN … THE SYSTEM SHALL …" requirements.
- [Google engineering practices](https://google.github.io/eng-practices/review/developer/small-cls.html): about 100 lines is a reasonable change, 1,000 is usually too large.
- [Design docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/), a former engineer's account: a one-to-three-page document for incremental work.
- [Google SRE example postmortem](https://sre.google/sre-book/example-postmortem/): one-sentence summary, action items as a table, timeline last.
