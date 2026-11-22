# 0006: Step handoff record and continuation under the next skill

Status: accepted

## Context

Each skill ended with a reply for a person. Two gaps follow from that.

- A capable host does not stop where a skill stops. Asked to accept a plan, a user answers "yes" and the host starts implementing, often because its own rules treat approval as permission to proceed. The work then runs outside the build skill, so that skill's checks and output rules do not apply.
- Nothing a program can read says whether a step finished, what it is waiting for, or what should run next. A pipeline cannot chain steps from prose, and a run with no user has nobody to answer a question.

## Decision

Add a step handoff section to the shared contract, inherited by every skill.

- A decision states what a "yes" will start.
- When the host continues, it loads and follows the next step's skill and says so. Acceptance authorizes the consuming step on that revision and nothing beyond it.
- Every step writes `handoff.json` beside its artifacts: step, status, outputs, awaited items, next skill and inputs, and how far the request authorizes the run.
- A run with no user never waits. It takes recorded defaults for minor questions, records what needs a person with status `waiting`, and stops.

The record is a file, not a block in the reply, because a pipeline reads files reliably and replies vary by host.

## Consequences

- Chained work stays inside the skills, whether a person or a pipeline drives it.
- A pipeline can branch on one small file instead of parsing output.
- The record is written by the model, so a pipeline must treat it as a report: it selects the next job, and the pipeline's permissions and required approvals decide whether that job may act.
- One file is replaced at each step, so it shows the latest state only. History stays in the artifacts and, where used, the evaluation log.
- Hosts follow such instructions with varying reliability. A host that still improvises the next step needs a host-level control, which this package does not ship.

## Sources

- [Anthropic: building effective agents](https://www.anthropic.com/engineering/building-effective-agents): prompt chaining with programmatic checks between steps.
- [Claude Code headless mode](https://code.claude.com/docs/en/headless): non-interactive runs for pipelines.
