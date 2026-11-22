# 0003: Interactive first, CI for review and verification

Status: accepted (22 November 2026)

## Context

The pack is used interactively: an engineer invokes one skill at a time in Codex or Claude Code. An alternative is to run the whole framework as GitHub Actions workflows, with an issue label producing a specification pull request, its approval producing a plan, and so on.

Vendor documentation reviewed on 22 November 2026 shows:

- No vendor documents an issue-to-specification pipeline. GitHub Spec Kit runs its steps in the agent's chat, one at a time. Google's Jules requires plan approval before code changes.
- Build is the stage vendors delegate to asynchronous agents (Copilot coding agent, Claude Code via mention, Jules), always ending in a pull request a human reviews.
- Review and verification run on pull request events and are advisory. Claude Code Review "never approves or blocks".
- Scans and triage run on schedules.
- Anthropic describes the same split for its own work: interactive coding, review agents when a pull request opens, periodic scans, and human final approval.
- Agents in CI that read issue or comment text have a documented prompt-injection record, and a workflow run shares one trust domain with its token and secrets.

## Decision

Do not run the whole framework as GitHub workflows. Recommend this split:

| Stage | Where it runs | What a human approves |
| --- | --- | --- |
| Discover, specify, design, plan | Interactive | Review and merge of the committed Markdown |
| Build | Interactive, or an asynchronous agent started by someone with write access from a merged specification and plan | Pull request review by someone other than the requester |
| Verify, review, security review | CI on `pull_request`, read-only | Nothing; findings are advisory |
| Security scanning, triage, improvement reports | Scheduled | The resulting issue or report |
| Release | Human-owned, with the release skill preparing the record | Environment required reviewers |

Ship one example workflow, `templates/github/ai-sdlc-pr-review.example.yml`, for the review stage. It is a template outside `.github/`, so it does not run in this repository.

Do not ship an issue- or comment-triggered workflow.

## Consequences

- The steps where judgment and clarification matter stay in a conversation, where the engineer can answer questions.
- State passes between stages as committed files, which is also what a later CI run can read. Workflow runs do not share memory.
- The example gives teams a starting point for the stage with the most vendor precedent. It needs the action pinned to a commit and a test-repository trial before use.
- Teams that want an issue-to-pull-request chain must design it themselves and accept the injection exposure. This pack does not help them do that.
- Not verified: whether the action can load a marketplace from a private repository.

## Sources

- [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions) and its [security notes](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md)
- [Claude Code Review](https://code.claude.com/docs/en/code-review)
- [How Anthropic secures its AI-native SDLC](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)
- [GitHub Spec Kit](https://github.com/github/spec-kit)
- [GitHub Agentic Workflows security architecture](https://github.blog/security/vulnerability-research/under-the-hood-security-architecture-of-github-agentic-workflows/)
- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use)
