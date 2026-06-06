# Task 001 Report: Linear Regression on California Housing

## Executive Summary

This report is intentionally unfilled.
Complete it only after you have run the baseline and Linear Regression yourself.

Use this report to answer three things clearly:

1. What did the model learn?
2. Where did it fail?
3. What would you change next, based on evidence?

---

## Task Metadata

| Field | Value |
|---|---|
| Task ID | 001 |
| Task | Linear Regression on California Housing |
| Phase | Phase 1 - Linear Models and Basic Tabular ML |
| Dataset | California Housing |
| Data Type | Tabular |
| Task Type | Regression |
| Best Model | TBD |
| Primary Metric | RMSE or MAE, with justification |
| Best Result | TBD |
| Status | IN_PROGRESS |

---

## Problem Statement

Fill this in after you have inspected the dataset yourself.

- What is being predicted?
- Why is this a regression problem?
- Why is Linear Regression a good first model here?

---

## Dataset Summary

| Field | Value |
|---|---|
| Source | `sklearn.datasets.fetch_california_housing` |
| Rows | 20,640 |
| Columns | 8 features plus target |
| Target | `MedHouseVal` |
| Missing Values | None in the cached scikit-learn frame |
| Notes | Original lineage traces to 1990 U.S. Census housing data |

Important dataset observations:

- Add your own notes here after EDA.

---

## Methods

### Baseline

Document:

- what the baseline predicts
- why it is a fair dumb comparison
- how you computed it without leakage

### Main Model

Document:

- exact Linear Regression setup
- any scaling choice and why
- train/test split details

### Preprocessing

Document:

- whether scaling was used
- whether any transformations were used
- why you kept or rejected them

---

## Results

| Model | MAE | RMSE | R^2 | Notes |
|---|---:|---:|---:|---|
| Mean Baseline | TBD | TBD | TBD |  |
| Linear Regression | TBD | TBD | TBD |  |

Interpretation prompts:

- Which metric best captures the difference between the two models?
- Did the model improvement feel large, modest, or disappointing?
- What does that say about the dataset and model assumptions?

---

## Visualizations

| Plot | Path | Purpose |
|---|---|---|
| Target distribution | `outputs/plots/target_distribution.png` | Understand skew and cap effects |
| Predicted vs actual | `outputs/plots/predicted_vs_actual.png` | Inspect fit quality |
| Residual plot | `outputs/plots/residuals.png` | Inspect systematic error structure |

---

## Error Analysis

Use this section to explain evidence, not vibes.

- Where are the largest errors?
- Are expensive homes harder to predict?
- Do you see geographic or distribution-driven failure patterns?
- Is the model missing nonlinear structure?

---

## What I Learned

- 

---

## What I Would Try Next

- 

---

## Final Verdict

State whether the task is complete and what should happen next.

Recommended next task:

- Task 002 - Regularized Regression on California Housing
