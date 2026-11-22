# S01 rerun under the output rules (package 0.3.0)

**Result:** partial. The outputs follow the new structure, but they are not shorter than the 0.2.1 outputs.
**Decision needed:** whether structure-first outputs of this length meet the reviewers' complaint, or the page target needs enforcing.
**Next owner:** package maintainer

## Measurements

| Artifact | 0.2.1 words | First rerun (rules 1 to 9) | Second rerun (with the page target) | Second rerun, body only |
| --- | --- | --- | --- | --- |
| Specification | 897 | 1,247 | 960 | 870 |
| Implementation plan | 625 | 1,115 | 770 | 630 |
| Decision record | 248 | 554 | 595 | not measured |

Body words exclude the `Record` block and collapsed sections. The routine target is about 400.

## What changed

- The status, decision needed and next owner are in the first four lines of each artifact.
- Open decisions are capped at three, each with a recommended answer and the requirement it blocks.
- Requirements are single "WHEN … THE SYSTEM SHALL …" rows; one-off constraints moved to assumptions (12 requirements in the first rerun, 9 in the second).
- The S01 criteria still hold: tenant boundary kept, CSV escaping left as an owner decision, shared test file given one writer, nothing executed.

## Limits

- One run per condition, each by a fresh subagent on a different model and host from the 0.2.1 run. Differences in length cannot be attributed to the rules alone.
- The first rerun's agent also applied the operator's own reply-format rules; the second was told the shared contract takes precedence.
- The decision template was not slimmed and has no summary or `Record` block; the agent added both.
- No no-skill baseline was run.
