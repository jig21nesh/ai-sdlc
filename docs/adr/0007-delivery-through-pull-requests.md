# 0007: Deliver through a definition pull request and stacked build slices

Status: accepted

## Context

[ADR 0003](0003-interactive-first-ci-for-review.md) makes review and merge of committed Markdown the approval for the early steps, and pull request review the approval for build. It does not say how many pull requests a change should produce or how they relate.

One pull request per step is the obvious mapping and a poor one:

- Nine steps give up to nine pull requests for one change, most holding a single document. Reviewers approve a small change faster and more carefully than a long queue.
- A change to the specification in review forces every pull request above it to be rebased and read again.
- Verify, review, security review and evaluate assess work; they produce nothing to merge.
- Release, incident and improvement records belong to a deployment or an event, not to the change's branch.

Stacking does help where each part is small, depends on the one before and can be reviewed alone. That describes build slices.

## Decision

Add a section to the shared contract:

- One definition pull request carries intent, specification and plan, or only the plan when a ticket carries the specification. Merging it accepts the plan.
- Build delivers one pull request per plan task, each based on the branch it depends on, merged from the bottom up.
- Assessing steps comment on the pull request they assess.
- Release, incident and improvement records are separate, when they occur.
- An open pull request is a `waiting` state in the handoff record; its merge is the answer.
- Pushing, opening and commenting need authority; merging stays with the reviewer.

## Consequences

- A change costs one definition review plus one small review per slice.
- The plan's task table doubles as the stack order, so the plan must keep tasks independent enough to review alone.
- Stacks need rebasing when a lower slice changes. Code hosts with native stacking reduce this; others need it done by hand or by the host.
- A definition pull request can still be long for a large change. Splitting it is allowed where the specification needs agreement first.
- Projects without pull requests are unaffected.

## Sources

- [Google engineering practices: small changes](https://google.github.io/eng-practices/review/developer/small-cls.html)
- [Anthropic playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook): human approval at review, with agents producing reviewable changes.
