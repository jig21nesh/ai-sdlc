# Retired pilot: recurring security scan proposal

Mode: plan-only, with limited triage of one supplied report. Scope is the retired pilot repository and deployment inventory. Authorization is offline proposal only. No scanner is configured; no scan, schedule, issue, notification, remote request, source upload or patch publication has occurred.

## Coverage and first useful step

Obtain an authoritative inventory of repository revision, dependency manifests, workflows/jobs, deployment resources, service identities and retained data. The supplied runtime facts are reported evidence, not live verification. Inventory inspection must cover the enabled reconciliation job because it may recreate a deleted deployment. Credential revocation and retained-data obligations require separate authoritative verification; a source scanner cannot prove either.

| Surface | Proposed method | Current coverage / limitation |
| --- | --- | --- |
| Source/configuration | Approved local static analyzer appropriate to actual languages | Not run; language, scanner, revision and rules unknown |
| Dependencies/build artifacts | Approved manifest/artifact scan with dated rules | Not run; manifests, artifact inventory and database absent |
| Secrets | Approved local secret scan with synthetic examples distinguished from actual credentials | Not run; only F1 report text supplied; file/history absent |
| Workflows/schedules/agent tools | Review triggers, tokens, trust boundaries and active resource reconciliation | Supplied nightly job is reported enabled; actual runtime not inspected |
| Deployment/identity inventory | Read-only authorized inventory and revocation-state evidence | Reported deployment deleted; token revocation unverified |
| Backups/retained records | Inventory, retention/hold owner decision and access verification | Backups reported retained; legal hold unknown; no destructive disposition |

Before any execution, identify scanner and rules versions, configuration and candidate digests, command and exit semantics, supported/excluded paths, local/remote data destinations, required identity, time/cost bounds, report retention and responsible operator. Prefer existing approved capabilities; do not install a suggested tool implicitly. Test scanner configuration using synthetic data in an authorized local environment. Treat timeout, unsupported language and partial scan as coverage gaps, not clean results.

## Proposed recurrence, pending owner decision

While residual assets remain, propose a weekly inventory/scan review plus a review after workflow, dependency, credential, deployment inventory or retention-policy changes. Weekly is a proposed temporary operational interval for this fixture, not an adopted policy or security guarantee. The security and operations owners must choose feasible cadence, approved scanner and evidence requirements. Suspend unnecessary recurrence only after owners verify retirement closure and decide what retained assets still need monitoring.

The operator should keep dated reports and stable finding identities, compare candidate/rule changes, link duplicates, and revisit dismissed findings when relevant inputs or exposure change. On a scan failure, preserve partial output, attempt at most one bounded retry after diagnosing a transient error, then produce a local failure draft for the responsible owner. Do not silently treat unavailable coverage as a pass. The actual runbook must name a notification destination and authorized delivery mechanism, emergency stop and operator; those values are currently unknown. This document neither sends notifications nor installs a schedule.

## F1 triage

See `finding-triage.json`. The provided content is an obvious-looking example marker, but the file, history, scanner and detection evidence are absent. The finding is unconfirmed; it is not a verified exposed credential and is not yet an evidence-backed false-positive dismissal. Inspect the actual candidate locally when available, check whether it is solely a synthetic fixture, and record a narrow dismissal only if that evidence supports it. Preserve the rule for real secrets; do not add a broad path/rule suppression to clear one marker.

## Evidence record and closure

Each future run must record command/tool/rules/configuration/candidate identity, time, environment, coverage, exit semantics, sanitized raw output and normalized finding dispositions. A supported bounded defect can become a scoped repair; broader issues require owned intent. Verify repairs at the actual changed revision and preserve outstanding coverage gaps. Current scan execution status: **not-run**. Proposal preparation is complete; operational acceptance and execution remain unperformed.
