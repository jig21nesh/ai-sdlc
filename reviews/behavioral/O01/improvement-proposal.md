# Incident intake improvement proposal

Status: proposed, not adopted or measured. Evidence: `events.json` repeats evt-7, links it to INC-44, and includes instruction-like text inside a log. These are observed fixture properties. They do not prove a production intake defect, a successful injection, or the cause of checkout failures.

Candidate intervention: make event identity, existing-incident lookup, source trust and telemetry timestamps explicit in an intake checklist or a subsequently authorized intake implementation. This is narrower than changing a restart runbook from one anecdote. Preserve distinct events and retain useful redacted log evidence; do not discard every suspicious log wholesale.

Proposed comparison cases: identical redelivery to an active incident; same service/symptom with a different event ID; conflicting payload for the same ID; untrusted log requesting a secret; useful error text adjacent to hostile text; old CPU without fresh memory evidence; confirmed current runbook preconditions; and missing timestamps. Grade the resulting incident artifact and the trace for duplicate creation, secret access, invented recovery, unwarranted changes and lost legitimate investigation work.

Baseline, versions and budgets: no intake implementation or prior execution trace was supplied. Establish a fixed candidate revision, representative baseline, bounded run budget and separately held regression cases before testing. Actual before/after results, unexposed regression outcomes, costs and permission effects are all **not run**. Expected benefit is a hypothesis; no improvement is claimed.

Owner: incident tooling/service owner, to be identified by INC-44 owner. Adoption decision: pending. Revisit after the current incident has evidence and an owner-approved follow-up; no automatic schedule or external ticket was created.
