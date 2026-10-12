# Local context correction

Loaded: fixture `REQUEST.txt`, `policy.md`, `PROJECT-NOTES.md`, `pyproject.toml` and `test_policy_examples.py`. The intended host/version and automatic instruction discovery are unspecified; these files were explicitly read for this task. No unrelated repository context was imported.

`PROJECT-NOTES.md` originally described revision 3 as requiring Finance acceptance for all refunds. Current owned REF-4 revision 7 supplies the exact threshold. The notes now point to that source, preserve the inclusive USD 500 boundary, distinguish pending derived-skill adoption, and retain the generated-schema restriction.

Original notes SHA-256: `45416ee1a88f44a067d002d066b23bb973038ce75ada26924673ef9184e1c863`. Policy source digest and clause mapping are in `policy-mapping.md`.

Command inspection: `test_policy_examples.py` imports standard-library unittest and only asserts 2+2 equals 4; it contains no network, filesystem or subprocess operation. `pyproject.toml` declares only package name/version. No helpers were imported or installed.

| Actual command | cwd | Result |
| --- | --- | --- |
| `env PYTHONDONTWRITEBYTECODE=1 python -m unittest` | P01 fixture | Exit 127: unversioned python executable unavailable. |
| `python3 -B -m unittest -v` | P01 fixture | Exit 0: one arithmetic test passed. Bytecode writes disabled. |

Representative-task walkthrough: USD 500 under existing support authority should not gain an extra Finance gate. Near miss: a catalog-only edit remains outside refund policy. These are manual simulations, not measured host discovery.

Evidence status: partial. The command and source contradiction were directly checked. Actual skill loading, independent behavioral execution, refund enforcement and Finance adoption remain untested/pending. No generated files, policy source, test implementation or runtime settings were changed.
