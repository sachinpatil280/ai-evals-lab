# Rules for this repo

## Identity rule (non-negotiable)

All commits and pushes in this repo belong to GitHub account `sachinpatil280` only. Never the work account (`patisac_kcglobal`, `@konecranes.com`).

- Author and committer: `sachinpatil280 <37938690+sachinpatil280@users.noreply.github.com>`.
- Push target: `https://sachinpatil280@github.com/sachinpatil280/ai-evals-lab.git`.
- Every `gh` command must run as `env -u GITHUB_TOKEN gh ...`. The shell's `GITHUB_TOKEN` is the work account.
- Enforced by `.githooks/` (pre-commit, commit-msg, pre-push). Never use `--no-verify`, never change `core.hooksPath`, `user.*`, `credential.*` or the remote. If a hook blocks, stop and report it; do not work around it.
- Fresh clone: `git config core.hooksPath .githooks` plus the local user/credential config before the first commit.

## Data rule

No employer data, code or user stories in this repo. Public or synthetic only.

## Stack

Python + pytest + DeepEval. Every deliverable runs via `pytest` or `deepeval test run`. See GOAL.md.
