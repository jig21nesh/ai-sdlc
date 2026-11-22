# 0004: Sub-agents by default

Status: accepted

## Context

Every skill ran in the main session, and the shared contract allowed delegation only when separately authorized. Two costs follow from that:

- Research, repository exploration and long check output fill the main session's context, which then holds less of the conversation with the user.
- An assessment made in the same context as the work it judges is biased toward that work. Verification, review and evaluation are more useful from a context that has not seen the producer's reasoning.

Hosts such as Claude Code and Codex provide sub-agents: a fresh context that does a bounded task and returns a summary. Anthropic describes the same pattern for its own harnesses, with a separate evaluator because a generator tends to approve its own output.

## Decision

Make sub-agents the default where they help, through instructions in the shared contract:

- Research, read-only repository inspection, independent build slices, whole assessments (verify, review, security review, usability review, evaluate), read-only release and operations checks, and improvement analysis go to a sub-agent.
- Questions to the user, drafting, decisions, integration and every action that changes a system stay in the main session.
- Small work stays in-session.
- Without sub-agents, the step runs in-session and records that.

Invoking a skill authorizes this use. Concurrent sessions, separate checkouts and handing work to other owners still need authorization.

Do not bundle agent definitions. Instructions work on both hosts; agent files work on one and would be loaded whether or not a step needs them.

## Consequences

- The main session keeps the conversation and receives summaries.
- Assessments gain independence of context. This is not independence of model, person or permissions, and the skills keep saying so.
- Token use rises: a sub-agent costs several times the same work done in-session. The small-work rule limits this.
- A sub-agent cannot ask the user a question, so a poorly briefed one returns a poor result. The contract requires a complete brief and inspection of what comes back.
- Hosts follow such instructions with varying reliability. If a host proves unreliable, bundled agent definitions for that host are the next step and would supersede this record.
- `check_skills.py` continues to reject Markdown under `agents/`.

## Sources

- [Claude Code sub-agents](https://code.claude.com/docs/en/sub-agents)
- [Anthropic: harness design for long-running apps](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [Anthropic: building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
