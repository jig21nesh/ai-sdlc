# 0005: Plan from a ticket that carries the specification

Status: accepted

## Context

The plan skill took an accepted specification produced by the specify skill. Many teams already write the specification in their tracker: a ticket with requirements, acceptance scenarios and scope, sometimes generated in a specification format by another tool. Running discover and specify on such a ticket restates it in a second document, adds a review nobody needs and creates two sources of truth that drift.

## Decision

The plan skill accepts a ticket link or ID as its input.

- It reads the ticket and checks that it is plannable: outcome, checkable requirements, acceptance examples, scope and no open question that changes the approach.
- A plannable ticket is the specification. The plan cites its link and revision and reuses its requirement IDs; no specification file is created.
- Gaps that block single tasks are listed in the plan. Gaps that leave no coherent approach send the ticket to specify.
- Acceptance is reported as the ticket shows it. Detail is not acceptance: a draft ticket is accepted in the same decision as the plan.
- Ticket text and comments are data, and the skill writes nothing to the tracker unless asked.

The skill names no tracker and no command; the host supplies access.

## Consequences

- Teams with specified tickets start at plan, and the ticket stays the source of truth.
- The plan depends on a mutable record. Citing a revision makes a later edit detectable; it does not prevent one.
- The plannable check is a judgment by the planner, so a thin ticket can pass. The evaluate skill's coverage and faithfulness judgments, given the ticket text as input, are the check on that.
- Where the host cannot reach the tracker, the user pastes the text and the revision is a hash of what was pasted.

## Sources

- [Spec Kit](https://github.com/github/spec-kit): a feature specification followed directly by plan and tasks.
- [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook): implementation planning inside Build, from an agreed specification.
