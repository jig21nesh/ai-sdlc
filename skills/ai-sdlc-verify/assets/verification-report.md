# Verification report

Record report ID/time, verifier, candidate revision or artifact digest, authoritative requirements/acceptance references, relevant profile versions and environment. State whether this is producer self-checking or independent verification.

## Scope

Separate software behavior, delivery-agent behavior and product-AI behavior. State why any scope is not applicable. Identify changed risks, baseline failures and unavailable environments.

## Behavior and proof matrix

| Requirement/risk ID | Expected observable behavior | Check and test data | Dependency realism and reason | Evidence/result | Gap or limitation |
| --- | --- | --- | --- | --- | --- |

## Execution records

| Check ID | Candidate/configuration identity | Tool/version and literal argv | Working directory/environment | Start/end | Exit/result | Redacted evidence |
| --- | --- | --- | --- | --- | --- | --- |

Use pass, fail, partial, blocked, not-run or not-applicable with reasons. Record skipped/zero-test outcomes explicitly. For a sensitivity experiment, identify the temporary defect/mutation, expected failing check, result and restoration verification.

## Findings and repairs

| Finding | Affected behavior and severity | Supporting evidence | Owner | Repair/candidate | Recheck result |
| --- | --- | --- | --- | --- | --- |

## Agent evaluation when applicable

Record suite revision, held-out-data handling, task/model/skill/tool versions, repeated-trial count where relevant, grader/calibration, observed outcomes, authority violations, costs and comparison baseline. Keep product-AI evaluation separate.

## Verdict and acceptance

State the extent of demonstrated behavior and outstanding required evidence. Record residual-risk decisions separately, with actual source and scope. A passing check is not authorization to release. Name the next owner and decision.
