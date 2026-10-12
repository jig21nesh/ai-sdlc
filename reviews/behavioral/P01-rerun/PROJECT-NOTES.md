# Refund fixture context

Applies to package `refund-fixture` version `0.0.1`, from `pyproject.toml`.

Use owned [REF-4 revision 7](policy.md): refunds above USD 500 require Finance acceptance for the exact refund record. At or below USD 500, support staff may act under existing role authority. This supersedes the revision-3 note saying all refunds require Finance approval. Do not log full card details. The policy does not apply to product catalog edits.

The derived [refund policy skill](drafts/refund-policy/SKILL.md) is a draft; Finance adoption is pending in [the mapping record](policy-mapping.md). No host discovery or runtime enforcement has been validated.

Validated local command in this environment: `python3 -B -m unittest -v`. The original `python -m unittest` command could not start because the unversioned `python` executable is unavailable. The one existing test checks arithmetic only and does not verify refund behavior.

Generated schemas live in `generated/` and are not directly edited.
