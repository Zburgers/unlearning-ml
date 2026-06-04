# Task XXX: Task Title

## Metadata

| Field | Value |
|---|---|
| Task ID | XXX |
| Slug | `xxx_task_slug` |
| Phase | Phase X — Phase Name |
| Status | TODO |
| Priority | P0/P1/P2/P3 |
| Data Type | Tabular / Text / Image / Audio / Time-Series / etc. |
| Task Type | Regression / Classification / Clustering / Forecasting / etc. |
| Dataset | Dataset Name |
| Target | Target variable, if applicable |
| Main Models | Model names |
| Main Metrics | Metric names |

---

## Goal

State the goal of this task in 2–4 sentences.

Explain what model family, data type, and ML concept this task is meant to teach.

---

## Learning Questions

- What is this task trying to predict, classify, cluster, or explain?
- What does the baseline do?
- What does the main model learn?
- Which metric matters most and why?
- Where can this model fail?
- What should be tried next?

---

## Dataset

### Source

- Dataset name:
- Source URL or library:
- License / usage notes:
- Download method:

### Shape

- Rows:
- Columns:
- Target:
- Feature types:

### Data Notes

- Missing values:
- Outliers:
- Known biases:
- Leakage risks:

---

## Models

### Baseline

- Model:
- Purpose:
- Expected behavior:

### Main Model

- Model:
- Why this model:
- Important assumptions:

### Optional Comparisons

- Model:
- Reason:

---

## Evaluation Plan

| Metric | Why It Matters |
|---|---|
| Metric 1 | Explanation |
| Metric 2 | Explanation |
| Metric 3 | Explanation |

Validation strategy:

- Train/test split:
- Cross-validation:
- Time-aware split, if applicable:

---

## Checklist

- [ ] Create or verify task folder structure
- [ ] Load dataset
- [ ] Document dataset source and target
- [ ] Run basic EDA
- [ ] Check missing values
- [ ] Check target distribution
- [ ] Create baseline
- [ ] Train main model
- [ ] Evaluate model
- [ ] Compare against baseline
- [ ] Save metrics to `outputs/metrics.json`
- [ ] Save plots to `outputs/plots/`
- [ ] Write `report.md`
- [ ] Update `EXPERIMENT_LOG.md`
- [ ] Update `PROGRESS.md`
- [ ] Update `TASKS.md`

---

## Expected Outputs

```txt
outputs/
├── metrics.json
├── predictions.csv
└── plots/
```

---

## Definition of Done

This task is DONE when:

- Dataset is documented.
- Baseline is implemented.
- Main model is implemented.
- Metrics are saved and explained.
- Errors/failure cases are analyzed.
- Final report is written.
- Global trackers are updated.

---

## Notes

Add task-specific notes here.
