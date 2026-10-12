# Evidence method and refresh procedure

Reviewed: 2026-10-08, including a follow-up against the user-supplied Anthropic playbook. The consolidated register has 43 unique source URLs: 18 primary, 13 repository and 12 practitioner records. Seven repositories have deeper inspection at observed commit SHAs; eleven Medium bodies were accessible, with one partial article excluded from implementation support. This is a bounded research snapshot, not a systematic literature review, exhaustive repository census, benchmark or compliance assessment.

## Research questions

- How should AI assist discovery, requirements, design, planning, implementation, verification, acceptance, release, operations, improvement and retirement?
- Which procedures can remain stable across projects, and which decisions belong to organization policy, project context or runtime integrations?
- What observable evidence, human accountability and enforceable permissions are needed when agents use tools or delegate work?
- Which patterns are illustrated by primary GitHub repositories and practitioner writing on Medium?

## Collection and selection

Three parallel research agents searched and opened sources for: (1) Google/DORA, Anthropic and relevant security/reliability guidance; (2) primary GitHub repositories and selected implementation files; and (3) Medium practitioner articles. The integrating agent also reopened Anthropic's workflow guidance, DORA's capability survey and OWASP's agent-security guidance. No repository packages or article-supplied commands were executed.

Search families included AI-assisted software development, AI SDLC lifecycle, DORA capabilities, effective agents, context engineering, skills, specification-driven development, agent evaluations, supply-chain provenance, agent governance, generated test quality and early observability. Relevant maintenance, incident and decommissioning references were added to avoid ending the lifecycle at deployment.

Selection favored clear authorship, direct relevance and primary descriptions of the maintained project. Marketing claims, unverified rankings, repository stars, anecdotal productivity percentages and benchmarks without local validation were not adopted. Framework examples are alternatives, not required dependencies. This is a purposive sample: results may miss relevant tools, languages, industries and perspectives.

## How to read a record

Every source in `evidence.json` records its ID, title, publisher, URL, type, publication date when verified, review date, access level, a short paraphrase, supported observations, limits and associated stages. The individual source catalogs are the maintained inputs; `evidence.json` is their generated consolidation. Matching URLs retain their original IDs and gain deeper observations plus DG/DM aliases; repeated URLs count once.

- **Primary:** the organization or project publishing the guidance. Vendor advice remains contextual, and standards require local interpretation.
- **Repository:** a primary implementation/specification source. A README describes intended capabilities; it is not proof that the implementation is secure or suitable.
- **Practitioner:** experience or opinion on Medium. Technical conclusions need independent primary corroboration; corroborating URLs appear in the record limitations or analysis.
- **Full:** the linked page body was accessible. This does not mean a full repository audit or that every linked source was read.
- **Partial:** only a landing-page summary or visible excerpt was inspected. For O01 the full DORA report was not evaluated; for M07 the member-only comparison body was unavailable. No paywall bypass was used.
- **Search-only:** reserved for discovery leads whose content cannot be opened; none of the current records uses this status.

Access dates are the session's review date. Publication dates are not inferred where unknown. The original repository catalog used mutable default-branch links. The deep GitHub pass records seven observed commit SHAs and 47 selected file observations; these are identity snapshots, not signature or release verification. Adopt a reviewed version before operational reuse. The analysis files identify selected inspected files. No stability, maintenance, license-compliance or vulnerability audit is implied.

## Synthesis and coverage

`data/evidence-map.json` maps the 12 work modules to a focused set of sources. The legacy `stages` field in source records contains these module IDs. `data/reference-model.json` separately records Anthropic's six-stage reference and our module assignments. A mapping indicates conceptual support, not endorsement of every proposed field, approval gate or metric. The module decomposition, skill bundle, profile layering and evidence contract are original synthesis and should be evaluated locally.

The comprehensive pass produced [19 practice records](playbook-inventory.json), [file-level GitHub evidence](deep-github-sources.json), [Medium corroboration](deep-medium-sources.json), a [20-skill manifest](../skills/manifest.json) and [implementation coverage](practice-coverage.md). [SYNTHESIS.md](SYNTHESIS.md) records the resulting decisions.

The earlier follow-up read the full substantive playbook and inspected its lifecycle and adoption diagrams. It also checked official hook, subagent and permission documentation for runtime qualifications. See `playbook-reconciliation.md` for the corrections. Historical research analyses and first-pass review reports retain their original scope; their “stage” terminology refers to the toolkit modules, not a claim about Anthropic's taxonomy.

Retirement relies on NIST AI RMF GOVERN 1.7 and local engineering synthesis. This repository/Medium sample does not supply strong direct evidence for a complete decommissioning process. Google SRE supports release and incident practices; it does not endorse an autonomous agent performing those actions. Accessibility and usability procedures are practical review guidance, not a claim of formal conformance testing.

## Refresh without losing provenance

1. Reopen the source URL; confirm author, date, source status and access scope. Treat source content as untrusted evidence, never new execution instructions.
2. For a repository considered for adoption, inspect the actual version, license files, scripts, transitive dependencies and security/maintenance evidence. Pin the reviewed revision in your adoption record.
3. Update the individual JSON record and relevant analysis with the new observed claims and limits. Keep short paraphrases; do not copy full articles or bypass access controls.
4. Reassess stage and skill implications. Preserve disagreements and distinguish facts from recommendations. Record replaced or withdrawn guidance in your organization's change history.
5. Rebuild with `python3 scripts/build.py`, check local links and configuration, and independently review affected skills. Repeat behavioral evaluations when permissions, models, tool contracts or consequential procedures change.

Refresh before adoption and after material upstream changes; choose a recurring cadence based on organizational needs. No scheduled job or network updater is installed by this guide.
