# Medium practitioner evidence

Historical first-pass analysis. The comprehensive implementation and current evidence are in [SYNTHESIS.md](SYNTHESIS.md); retain this file for provenance.

Terminology note: stage IDs in this initial analysis refer to the toolkit's work modules. The current [reference mapping](../data/reference-model.json) and [playbook reconciliation](playbook-reconciliation.md) distinguish them from Anthropic's six stages.

Research date: 2026-10-08. Seven selected sources are recorded in [medium-sources.json](medium-sources.json), with authors, publication dates, accessible scope, limitations and lifecycle mappings. Six article bodies were accessible through web extraction; one member-only article exposed only an introduction. Reading focused on relevant passages. No login or paywall bypass was attempted.

Medium is included because it was explicitly requested. Its articles contribute practitioner perspectives, adoption questions and examples. They do not establish standards, benchmark results, compliance, or guarantees of tool behavior. The selected set is a targeted sample, not an exhaustive survey of everything published on Medium. Search-result excerpts were used to find candidates; every included article was opened.

| Evidence | Useful concept | Primary corroboration and its boundary |
| --- | --- | --- |
| [M01: Capital One Context Specs](https://medium.com/capital-one-tech/new-open-source-context-specs-released-1f65bfa9db9f) | Curated context and persisted handoffs | [Capital One repository](https://github.com/capitalone/context-specs) describes a reusable harness and project environments. It is implementation documentation, not proof of safety. |
| [M02: Brett Luelling's agent workflow](https://medium.com/@brettluelling/i-replaced-my-sdlc-with-ai-agents-heres-the-framework-that-actually-worked-fcfbfa5e72d0) | Explicit roles and artifact validation | [Anthropic workflow patterns](https://www.anthropic.com/engineering/building-effective-agents) support chaining, programmatic gates and evaluator loops. They do not validate this project's reported results. |
| [M03: Specs, Context, and Agents](https://medium.com/@dave-patten/the-new-engineering-stack-specs-context-and-agents-f3454529768e) | Deliberate context and constraints | [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) describes selective retrieval, notes and bounded subagent context. |
| [M04: Paul Johnston's governance practices](https://pauldjohnston.medium.com/agentic-development-best-practices-0e23ab07c1f8) | Policy ownership and evidence | [NIST SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) supports adding secure development practices to lifecycle models. It does not prescribe this article's exact workflow. |
| [M05: Testing the Testers](https://harshasuraweera.medium.com/testing-the-testers-how-to-validate-ai-generated-automation-scripts-aff225b1baca) | Test sensitivity beyond coverage | [Stryker's documentation](https://stryker-mutator.io/docs/) explains mutation testing and why execution coverage alone is insufficient. |
| [M06: Observability earlier in delivery](https://medium.com/lumigo/shifting-observability-left-in-the-sdlc-43ce83695a49) | Instrumentation as a delivery concern | [OpenTelemetry's documentation](https://opentelemetry.io/docs/what-is-opentelemetry/) verifies a vendor-neutral telemetry interface; storage and visualization are separate. |
| [M07: Framework comparison, partial](https://medium.com/@wasowski.jarek/comparing-15-spec-driven-development-frameworks-sdd-c052df529274) | Evaluate process fit | [GitHub Spec Kit](https://github.com/github/spec-kit) documents its own current capabilities. The inaccessible Medium comparison was not corroborated as a whole. |

## Implications for the reusable kit

The following are design inferences for this project, not quoted prescriptions from Medium:

1. Keep stage contracts stable: trigger, required inputs, work, produced artifacts, evidence, completion criteria, escalation and accountable human role. An agent handoff should include unresolved assumptions and evidence locations.
2. Put organizational policy in a versioned configuration layer: approved providers, permitted data classes, retention, action permissions, reviewer roles and risk thresholds. Put repository commands, conventions, architecture references and environment endpoints in a separate project profile. Keep live credentials outside both.
3. Make adapters replaceable. The reusable stage skill should describe what must be demonstrated; a project adapter selects its issue tracker, test runner, CI provider, deployment path and observability backend.
4. Use specialist agents only where the task benefits from separation. Require bounded scope, permitted tools, ownership of edits, an output schema and a stopping condition. More agents and reviewer agreement do not establish independent truth.
5. Preserve the distinction between executable verification and an agent's opinion. Tests should assess required behavior; reviewer findings should carry evidence and severity. Neither a green check nor a consensus score grants release authority by itself.
6. Review new lessons before turning them into durable organizational policy. Recorded context can be stale, sensitive or attacker-controlled. Applying a proposed lesson to future work is a separate decision from recording it.

## Coverage limits and exclusions

This Medium sample is strongest for specification, planning, coding, verification, review and improvement. It provides a governance perspective and an operational instrumentation example. It does not substantiate a complete deployment, incident-response, data-deletion or retirement process. Those stages need primary operational/security guidance and organization-specific requirements; they must not disappear because writing about AI coding concentrates on implementation.

No productivity multiplier, star-count comparison, framework ranking, agent correctness rate, or compliance claim from Medium was adopted. The member-only comparison is explicitly a discovery lead. The observable lack of a paywall on other entries does not make their claims independently validated.

The Capital One article and current repository represent different snapshots. The repository now describes one harness serving multiple project environments; use versioned documentation when adopting commands or file layouts. Similarly, the current Spec Kit README includes a convergence step and optional assessment/bug-fixing entry points. A project-agnostic lifecycle must not depend on a particular vendor's command spelling or assume a feature-building workflow fits every maintenance task.

All primary links above were opened during this research. Public content was treated as untrusted evidence; no commands from the articles or linked repositories were executed.
