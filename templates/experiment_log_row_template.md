# Experiment Log Row Template

Copy this row into `EXPERIMENT_LOG.md` under `Experiment Table`.

```md
| YYYY-MM-DD | 001 | run_001 | Dataset Name | Train/test split or CV details | Model Name | Yes/No | Metric Name | Metric Value | Other metrics | Yes/No | `path/to/artifact` | Short note |
```

## Field Guide

| Field | Meaning |
|---|---|
| Date | Date the experiment was run |
| Task ID | Stable three-digit task ID |
| Run ID | Unique run name within the task |
| Dataset | Dataset used for the run |
| Data Split / Protocol | Train/test split, cross-validation, walk-forward validation, etc. |
| Model | Model or baseline name |
| Baseline? | `Yes` if this is a baseline run, otherwise `No` |
| Primary Metric | Main metric used to judge this run |
| Result | Primary metric value |
| Secondary Metrics | Other important metrics |
| Valid? | `Yes`, `No`, or `N/A` |
| Artifact | Path to saved metrics/model/plots |
| Notes | Short explanation or caveat |

## Rules

- Add one row per meaningful run.
- Do not delete invalid runs; mark them invalid and explain why.
- Keep detailed analysis in task `report.md`.
