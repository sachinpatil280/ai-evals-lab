# Goal

**Target:** AI/LLM Quality Lead → Quality Architect for AI-enabled systems, with EU AI Act governance fluency as the differentiator.

**Background:** 13 years in QA, ~10 as SDET.

**Rule:** If it is not in this repo and runnable via `pytest` / `deepeval test run`, it does not exist.

## Use case

**LLM-generated test cases from user stories.**
Input: a user story with acceptance criteria. Output: structured test cases (Title, Preconditions, Steps, Expected).
Why: I am the domain expert judge here, which makes human-calibration labels credible.
Data: public or synthetic user stories only. No employer data.

## Stack (fixed)

- Python + pytest, DeepEval (`assert_test()` threshold gates)
- Phase 2 additions: RAGAS (inside DeepEval/pytest), Promptfoo (secondary entry point for red teaming), self-hosted Opik or Langfuse
- Not in core stack: LangChain, LlamaIndex

## Phases and checkpoints

Start: 2026-11-10. Commitment: 8–10 hrs/week.

| Phase | Due | Checkpoint (pass/fail) |
|---|---|---|
| 0 | 2026-11-23 | Public repo, this doc, stack runnable (`deepeval test run tests/` passes) |
| 1 | 2027-02-10 | 50–100 example golden dataset; rubric → LLM-as-judge → human labels on 20 samples → judge-vs-human agreement rate reported |
| 2 | 2027-05-10 | Eval gated in GitHub Actions with justified threshold; one Promptfoo safety test; tracing; EU AI Act requirement → test-type mapping (1 page) |
| 3 | 2027-11-10 | One real team adopts the pipeline; measured impact; one public presentation |
| 4 | 2028-11-10 | Lead/Principal/Architect title with AI quality ownership; 2–3 published writeups with measured results |

**Month-12 rule (2027-11-10):** no AI quality scope from my employer by then means I change employers.

## Run

```
git config core.hooksPath .githooks   # identity guard, once per clone
uv sync
uv run deepeval test run tests/
```
