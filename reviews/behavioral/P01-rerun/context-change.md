# Context change record

Candidate: supplied refund-fixture 0.0.1 raw files. Scope: local guidance and refund-policy skill draft. Intended consumer: a future selected agent host; none was specified, so discovery/precedence remain untested.

Read `REQUEST.txt`, `policy.md`, `PROJECT-NOTES.md`, `pyproject.toml` and `test_policy_examples.py`. The owned revision-7 policy explicitly permits existing support authority at/below USD 500; it contradicts the older revision-3 all-refunds approval note. Replaced that specific stale guidance and retained the generated-schema rule. The policy source, manifest and test implementation were not modified.

Inspected test implementation before running: Python unittest with one arithmetic assertion, no external calls or hooks. In this case directory, `env PYTHONDONTWRITEBYTECODE=1 python -m unittest` failed with exit 127 (`python` absent); `python3 -B -m unittest -v` passed with exit 0, one test. Updated the command to the observed working executable, recording its environment limit instead of changing dependencies.

Manual representative checks: USD 500 now maps to existing support authority; USD 500.01 requires exact-record Finance acceptance; catalog edits remain outside the policy. These are document simulations, not agent-host discovery tests or payments. No unrelated memory or global instruction files were created.
