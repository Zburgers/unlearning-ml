# Unlearning ML Task Tracker

This file is the global execution board for the repository.

It should answer three questions quickly:

1. Where is the project right now?
2. What is the active task?
3. What should be done next?

For detailed task work, use the task folder.  
For final results, use the task report.  
For daily notes, use `PROGRESS.md`.  
For experiment metrics, use `EXPERIMENT_LOG.md`.

---

## Tracker Metadata

| Field | Value |
|---|---|
| Project | Unlearning ML |
| Tracker Version | v1 |
| Last Updated | 2026-06-04 |
| Current Phase | Phase 1 — Linear Models and Basic Tabular ML |
| Current Sprint | Sprint 1 — Foundations |
| Active Task | 001 — Linear Regression: California Housing |
| Next Task | 002 — Ridge/Lasso: California Housing |
| Overall Status | STARTING |

---

## Status Legend

Use these exact status values so humans and AI agents can update this file consistently.

| Status | Meaning |
|---|---|
| TODO | Planned but not started |
| IN_PROGRESS | Task folder/code exists and work has started |
| EXPERIMENTING | Models are being trained, evaluated, or compared |
| REPORTING | Results exist; README/report/log updates are pending |
| DONE | Task meets the definition of done |
| BLOCKED | Task cannot continue without a decision, dataset, dependency, or fix |
| NEEDS_REVIEW | Task is mostly complete but needs verification |

---

## Priority Legend

| Priority | Meaning |
|---|---|
| P0 | Current active task |
| P1 | Start soon after active task |
| P2 | Planned backlog |
| P3 | Future/optional |

---

## Current Focus

```txt
Current task: 001_linear_regression_california_housing
Main goal: Relearn the complete regression workflow using a simple interpretable model.
Immediate next action: Create the task folder and add the task README/report/output structure.
```

---

## Sprint 1 — Foundations

| ID | Task | Phase | Dataset | Model Family | Priority | Status | Next Action |
|---|---|---|---|---|---|---|---|
| 001 | Linear Regression: California Housing | Phase 1 | California Housing | Linear Models | P0 | TODO | Create task folder and seed task README |

---

## Active Task Detail

### 001 — Linear Regression: California Housing

| Field | Value |
|---|---|
| Task ID | 001 |
| Slug | `001_linear_regression_california_housing` |
| Phase | Phase 1 — Linear Models and Basic Tabular ML |
| Status | TODO |
| Priority | P0 |
| Data Type | Tabular regression |
| Dataset | California Housing |
| Target | Median house value |
| Main Models | Mean baseline, Linear Regression |
| Main Metrics | MAE, RMSE, R² |
| Task Folder | `tasks/001_linear_regression_california_housing/` |
| Report Path | `tasks/001_linear_regression_california_housing/report.md` |
| Outputs Path | `tasks/001_linear_regression_california_housing/outputs/` |

#### Goal

Learn the full supervised regression workflow using a simple interpretable model before moving into regularization, nonlinear models, and deep learning.

#### Core Learning Questions

- What does a regression model predict?
- What is the difference between a dumb baseline and a learned model?
- How do MAE, RMSE, and R² explain model performance differently?
- What do residuals reveal about model failure?
- What assumptions does Linear Regression make?
- Where does Linear Regression fail on real housing data?

#### Required Checklist

- [ ] Create `tasks/001_linear_regression_california_housing/`
- [ ] Create `tasks/001_linear_regression_california_housing/README.md`
- [ ] Create `tasks/001_linear_regression_california_housing/report.md`
- [ ] Create `tasks/001_linear_regression_california_housing/outputs/`
- [ ] Load the California Housing dataset
- [ ] Document dataset source, rows, features, and target
- [ ] Perform basic EDA
- [ ] Check missing values and basic distributions
- [ ] Create train/test split
- [ ] Build a mean-value baseline predictor
- [ ] Train Linear Regression
- [ ] Evaluate baseline with MAE, RMSE, and R²
- [ ] Evaluate Linear Regression with MAE, RMSE, and R²
- [ ] Compare baseline vs Linear Regression
- [ ] Plot predicted vs actual values
- [ ] Plot residuals
- [ ] Save metrics to `outputs/metrics.json`
- [ ] Save plots under `outputs/plots/`
- [ ] Write final findings in `report.md`
- [ ] Update `EXPERIMENT_LOG.md`
- [ ] Update `PROGRESS.md`
- [ ] Mark task as DONE in this file

#### Definition of Done

Task 001 is DONE only when:

- The task folder exists.
- The dataset and target are documented.
- A dumb baseline is implemented.
- Linear Regression is implemented.
- Baseline and Linear Regression metrics are compared.
- Residual analysis is included.
- `outputs/metrics.json` exists.
- `report.md` explains what worked, what failed, and what to try next.
- `EXPERIMENT_LOG.md` has at least one row for this task.
- This tracker has been updated.

#### Notes

- Keep this task simple and clean.
- Do not add Ridge, Lasso, or ElasticNet here unless used only as a short preview.
- Regularization belongs in Task 002.
- The goal is workflow mastery, not leaderboard performance.

---

## Backlog

Backlog tasks should be appended here only after the current active task has enough structure.

| ID | Task | Phase | Data Type | Model Family | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|

---

## Completed Tasks

Move completed task summaries here after they are marked DONE.

| ID | Task | Completed Date | Best Model | Main Metric | Report |
|---|---|---|---|---|---|

---

## Blockers

| Date | Task ID | Blocker | Owner | Status | Resolution |
|---|---|---|---|---|---|

---

## Agent Update Instructions

When updating this file:

1. Update `Tracker Metadata` if the active task, phase, sprint, or overall status changes.
2. Update the task row in the sprint/backlog table.
3. Update the active task checklist only for the current task.
4. Do not add long experiment explanations here.
5. Put detailed experiment notes in the task folder.
6. Put final findings in `report.md`.
7. Put metric rows in `EXPERIMENT_LOG.md`.
8. Put day-by-day progress in `PROGRESS.md`.
9. Keep task IDs stable once created.
10. Append new tasks instead of renumbering old tasks.

This file should stay readable as a control board, not become a notebook or report.
