# Refund fixture context

Applicable package: `refund-fixture` version `0.0.1` from `pyproject.toml`.

Refund policy source: `policy.md`, REF-4 revision 7, owned by Finance. Above USD 500 requires Finance acceptance for the exact refund record; at or below USD 500 support staff may act under existing role authority. The revision-3 statement requiring Finance acceptance for every refund is superseded. Full card details must not appear in logs. Product catalog edits are outside this policy.

The derived procedure in `drafts/refund-policy/SKILL.md` is a local draft; Finance approval is pending and no agent-host discovery or payment enforcement has been established.

Validated local test command from this fixture directory: `python3 -B -m unittest -v`. The unversioned `python` executable was unavailable in the review environment. The existing test is an arithmetic smoke check only; it does not test refund policy or skill behavior.

Generated schemas live in `generated/` and are not directly edited.
