# Unlearning ML Progress Log

This file is the session-by-session progress journal for the repository.

Use this file to record what changed, what was learned, what is blocked, and what should happen next.

Do not put detailed experiment results here. Put metrics in `EXPERIMENT_LOG.md` and final task findings in the task `report.md`.

---

## Update Rules

1. Append new entries at the top of `Progress Entries` so the latest work is easiest to read.
2. Use the date format `YYYY-MM-DD`.
3. Keep entries concise and action-oriented.
4. Link to task IDs and files when possible.
5. Do not rewrite older entries unless fixing a typo or broken link.
6. If a task status changes, also update `TASKS.md`.
7. If experiment metrics are produced, also update `EXPERIMENT_LOG.md`.
8. If a blocker appears, also update the `Blockers` section in `TASKS.md`.

---

## Current Project State

| Field | Value |
|---|---|
| Project | Unlearning ML |
| Current Phase | Phase 1 — Linear Models and Basic Tabular ML |
| Current Sprint | Sprint 1 — Foundations |
| Active Task | 001 — Linear Regression: California Housing |
| Current Status | Global repo hygiene pass complete; ready to start Task 001 scaffold |
| Last Updated | 2026-06-04 |

---

## Entry Template

Copy this template when adding a new entry.

```md
## YYYY-MM-DD — Short Session Title

### Scope
- Task:
- Files touched:

### Completed
- 

### Learned
- 

### Problems / Blockers
- 

### Decisions
- 

### Next
- 
```

---

## Progress Entries

## 2026-06-04 — Global Repo Hygiene Pass

### Scope
- Task: Repo hygiene before Task 001
- Files touched: `DATASET_INDEX.md`, `MODEL_INDEX.md`, `NOTES.md`, `data/README.md`, `docs/`, `requirements.txt`, `pyproject.toml`, `.gitignore`, `src/unlearning_ml/`, `scripts/`, `tests/`, `AGENTS.md`, `PROGRESS.md`

### Completed
- Initialized empty global index files for datasets and models.
- Initialized global notes and data handling documentation.
- Filled support docs for repo philosophy, ML workflow, metrics, evaluation safety, experiment planning, and reading resources.
- Added minimal Python project config, requirements, and gitignore policy.
- Added small reusable utility helpers for paths, seeding, loading, validation, preprocessing, metrics, feature selection, plotting, and basic model factories.
- Added lightweight tests for reusable data, preprocessing, feature, and metric helpers.
- Hardened `AGENTS.md` with startup sequence, scoped update rules, dataset/model update rules, and commit/push workflow.

### Learned
- Several global files were still empty placeholders after skeleton creation.
- The repo needed explicit file ownership rules so future agents update only the correct scope.
- Task 001 can now begin without needing more global setup.

### Problems / Blockers
- No blockers.

### Decisions
- Do not touch Task 001 README/report files during this global hygiene pass.
- Keep reusable `src/` helpers minimal and task-agnostic.
- Keep deep learning, probabilistic, clustering, and ranking modules as placeholders until their phases become active.

### Next
- Create `tasks/001_linear_regression_california_housing/`.
- Seed Task 001 README, report stub, outputs folder, and starter implementation files.
- Update `TASKS.md` from TODO to IN_PROGRESS when Task 001 scaffold begins.

## 2026-06-04 — Tracking System Initialized

### Scope
- Task: Project setup / tracking workflow
- Files touched: `ROADMAP.md`, `TASKS.md`, `AGENTS.md`, `PROGRESS.md`, `EXPERIMENT_LOG.md`, `templates/`

### Completed
- Finalized the long-term roadmap in `ROADMAP.md`.
- Initialized `TASKS.md` as the global execution board.
- Seeded Task 001: Linear Regression on California Housing.
- Added update and append rules for progress tracking.

### Learned
- `TASKS.md` should track global execution state, not full experiment reports.
- `PROGRESS.md` should capture session notes and decisions.
- `EXPERIMENT_LOG.md` should capture compact metrics and reproducible experiment summaries.

### Problems / Blockers
- No blockers yet.

### Decisions
- Start with Task 001 before adding a large task backlog.
- Keep the first task focused on simple Linear Regression only.
- Keep Ridge, Lasso, and ElasticNet for Task 002.

### Next
- Create `tasks/001_linear_regression_california_housing/`.
- Add the task README, report stub, outputs folder, and starter notebook/script structure.
