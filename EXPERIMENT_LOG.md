# Unlearning ML Experiment Log

This file is the compact, append-first experiment results ledger for the repository.

Use this file to track experiment outcomes across tasks in a consistent format.

Detailed explanations belong in task-level `report.md` files. Daily/session notes belong in `PROGRESS.md`.

---

## Update Rules

1. Add one row per meaningful experiment run.
2. Keep rows compact and comparable.
3. Use stable task IDs such as `001`, `002`, `003`.
4. Use the date format `YYYY-MM-DD`.
5. Always include the dataset, model, split/evaluation protocol, and primary metric.
6. Do not delete old experiment rows unless they were accidental duplicates.
7. If an experiment is invalid, keep the row and mark `Valid?` as `No`, then explain why in `Notes`.
8. If metrics are saved to a file, link the `metrics.json` path in the `Artifact` column.
9. When a task is completed, make sure the best run is reflected in the task `report.md`.
10. Keep this file as a results index, not a narrative report.

---

## Current Experiment State

| Field | Value |
|---|---|
| Project | Unlearning ML |
| Active Task | 001 — Linear Regression: California Housing |
| Current Status | No experiments run yet |
| Last Updated | 2026-06-04 |

---

## Experiment Table

| Date | Task ID | Run ID | Dataset | Data Split / Protocol | Model | Baseline? | Primary Metric | Result | Secondary Metrics | Valid? | Artifact | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06-04 | 001 | planned | California Housing | Train/test split | Mean baseline, Linear Regression | Yes | RMSE/R² | TBD | MAE | N/A | `tasks/001_linear_regression_california_housing/outputs/metrics.json` | Task planned; no experiment run yet. |

---

## Row Template

Copy this row format when adding a new experiment.

```md
| YYYY-MM-DD | 001 | run_001 | Dataset Name | Train/test split or CV details | Model Name | Yes/No | Metric Name | Metric Value | Other metrics | Yes/No | `path/to/artifact` | Short note |
```

---

## Run ID Convention

Use this format inside each task:

```txt
run_001
run_002
run_003
```

Examples:

```txt
001_run_001_mean_baseline
001_run_002_linear_regression
001_run_003_linear_regression_scaled
```

Prefer readable run names when there are multiple variants.
