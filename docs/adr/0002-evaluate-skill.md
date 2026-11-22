# 0002: Evaluate skill and feedback loop

Status: accepted

## Context

The pack had no way to measure whether a step's output was good, so its quality could not be compared between versions. `ai-sdlc-agent-evals` designs controlled experiments on skills and models; it does not score the output of an ordinary run. `ai-sdlc-improve` needs measured failures as input and had no routine source of them.

Published guidance from Anthropic, OpenAI, Google and practitioners agrees on the design: deterministic checks first, one binary judgment per dimension with a written critique, a judge that sees the step's input, and calibration against a human's labels.

## Decision

Add a 21st skill, `ai-sdlc-evaluate`, that scores one step's output against its input.

- A standard-library script, `scripts/check_artifact.py`, performs the structural checks from the output rules (ADR 0001): decision-first summary, required sections, trailing record block, caps on questions, nits, table width, paragraph and body length, and coverage of the input's IDs.
- The agent then gives one verdict per dimension: coverage, faithfulness, decision clarity, actionability and concision. Verdicts are pass, fail or unknown. Concision is two-sided (too thin, right, too verbose) so that terseness is not rewarded.
- Each run appends one JSON line to a log in the product repository, including the skill version, file hashes and the human verdict.
- `summarize` counts failures per step and skill version. `ai-sdlc-improve` reads that summary, changes the smallest cause and keeps the failing artifact as a regression case.
- Caps and judgment questions live in one file, `references/rubrics.json`.

The script ships inside the skill so that it travels with the plugin on both hosts. Its tests live in `tests/` and run under `coverage` through `uv run`; nothing is added to the package's dependencies.

## Consequences

- Output quality and length become counts per step and version that can be compared across releases.
- The judgments are uncalibrated until a reviewer labels about 30 outputs. Until then they indicate trends and must not gate anything.
- A judge in the same session as the producer is biased toward its own work. The record states `independence` so that self-judged runs can be discounted.
- Skills tuned to the rubric can score better without reviewers being happier. The human verdict in each record is the anchor.
- The pack now ships executable code. It reads only the paths it is given, refuses files over 2 MB and non-regular files, and never executes artifact content.
- The skill count becomes 21; the manifest, README and plugin descriptions change with it.
