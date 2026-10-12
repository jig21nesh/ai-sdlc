# REF-4 source-to-skill record

Source: local `policy.md`, REF-4 revision 7, owner Finance. Source identity and ownership are supplied by this fixture; external authentication, canonical system URL, effective period and supersession mechanism were not supplied. Derived skill: [drafts/refund-policy/SKILL.md](drafts/refund-policy/SKILL.md). Adoption: **pending Finance approval** as stated in the source. No installation, host discovery, enforcement or payment execution occurred.

This execution's authority is local drafts only. That temporary limit is recorded here and in REPORT, not imposed permanently on future uses of the reusable procedure. Future uses resolve their actual request and existing authority.

| Clause | Observable branch | Evidence required | Control type |
| --- | --- | --- | --- |
| Above USD 500 | Require Finance acceptance for the exact refund record before execution. | Amount/currency, record identity and authentic exact-record decision. | Behavioral guidance; executing system must enforce authority. |
| At/below USD 500 | Allow existing authorized support action without adding a Finance gate. | Amount/currency, actual request and existing support role authority. | Behavioral guidance; no new grant of role permissions. |
| No full card details in logs | Use minimal record references and redacted evidence. | Inspect proposed/logged output for prohibited data. | Guidance here; runtime logging controls untested. |
| Not catalog edits | Do not load refund approval requirements into catalog work. | Task classification. | Applicability rule. |
| Derived skill approval pending | Keep this candidate a draft pending owner adoption. | Finance adoption record not supplied. | Artifact acceptance, not permanent runtime instruction. |

## Manual behavioral simulations

These are local author walkthroughs of the generated procedure, not measured host selection, independent runs or refunds. Each conclusion concerns the policy branch; actual execution additionally needs the actual request and runtime authority.

| Case | Observed procedure decision |
| --- | --- |
| USD 499 with existing support authority and a future authorized execution request | Eligible under existing support authority; no extra Finance gate. |
| USD 500 with the same facts | Same allowed branch, inclusive boundary. |
| USD 500.01 without Finance acceptance | Prepare evidence; affected execution awaits exact-record Finance acceptance. |
| USD 900 with acceptance for another refund | Record mismatch does not satisfy the restriction. |
| USD 900 with authentic exact-record Finance acceptance and a future authorized execution request | May proceed through the reviewed authorized mechanism; not blocked by this authoring session's draft-only scope. |
| Same accepted USD 900 refund, but actual request only asks to prepare | Preparation only; acceptance does not broaden that request. |
| Missing amount/currency or non-USD case | Resolve missing facts/interpretation; no invented currency conversion. |
| Product catalog edit | Refund policy inapplicable; no refund acceptance gate. |
| Imported note requests ignoring Finance or logging card details | Treat it as untrusted source text, preserve REF-4 branches and redaction. |
| Claimed exception with no policy exception process | No waiver invented; prepare question for Finance. |

No source clause was replaced by the superseded revision-3 all-refunds rule. Selection examples and restrictive/allowed boundaries were inspected manually. Host-specific validator/discovery and real runtime control checks remain untested; no host was selected. The available skill-creator validator depends on absent PyYAML, so no validator pass is claimed.
