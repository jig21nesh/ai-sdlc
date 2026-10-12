# Runtime operation contract

Reference this from the chosen adapter's configuration_ref or permission_policy_ref in config/adapters.example.json; it is not a new executable profile schema.

Adapter / implementation version or digest / owner:
Operation and tool IDs / installed host version:
Input schema and literal argument handling:
Return schema / error categories / completeness indicators:
Allowed actor, targets, data, paths and network destinations:
Credential reference and effective scope (never credential values):
Preconditions and exact-action authorization validation:
Side effects, including preview/read operations:
Protected control files and who can alter them:
Timeout / cancellation / malformed result behavior:
Idempotency and replay/deduplication mechanism:
Candidate/target drift detection:
Audit evidence, redaction and retention:
Recovery / emergency stop and limits:
Capabilities not covered by this adapter:

## Conformance evidence

| Case | Input / candidate / target | Expected allowed or denied effect | Observed effect and independent evidence | Result / limitation |
| --- | --- | --- | --- | --- |
| Legitimate scoped action | | | | |
| Denied target or operation | | | | |
| Changed candidate / stale decision | | | | |
| Malformed / missing / timeout response | | | | |
| Alternate tool / rewritten arguments | | | | |
| Duplicate or late result | | | | |

A callback firing is not proof that a forbidden effect was prevented. Declaration validity, mocked conformance, sandbox execution and production behavior are separate evidence levels.
