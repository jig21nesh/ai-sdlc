# Local skill task exercises

`cases.json` contains ten synthetic requests and raw artifacts. `rubric.json` records integrating-review criteria. These are development regression examples, not a representative dataset, untouched holdout or evidence of automatic host selection.

Copy each case's artifacts and request to a separate temporary directory. Give an authorized evaluator only that request, its raw artifacts and the indicated skill paths. Restrict writes to the fixture and disallow live external actions. For code tasks, inspect the fixture before running local tests. Evaluate actual output, resulting files, command results and side effects against the accepted request; do not score merely matching report wording.

The recorded run used three existing agents for cross-author exercises because creating a new agent hit the thread limit. They retained research context, received no target verdict or rubric, and were not a blinded fresh-session sample. S01 additionally used the evaluator's authored planning skill alongside others' skills. No no-skill/prior-version comparison was run, so the outcomes do not demonstrate causal improvement.

[Current validation](../../reviews/deep-validation.md) records results, method and gaps. Preserved artifacts are under `reviews/behavioral/`. Runtime discovery, actual hooks, cloud deployment, recurring scanners and browser/assistive-technology behavior require separate authorized integration tests.
