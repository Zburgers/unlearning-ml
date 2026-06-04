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
| Current Status | Repo tracking system initialized; Task 001 planned but not started |
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
