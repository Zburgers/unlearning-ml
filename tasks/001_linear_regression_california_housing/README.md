# Task 001: Linear Regression on California Housing

## Metadata

| Field | Value |
|---|---|
| Task ID | 001 |
| Slug | `001_linear_regression_california_housing` |
| Phase | Phase 1 - Linear Models and Basic Tabular ML |
| Status | IN_PROGRESS |
| Priority | P0 |
| Data Type | Tabular |
| Task Type | Regression |
| Dataset | California Housing |
| Target | `MedHouseVal` |
| Main Models | Mean baseline, Linear Regression |
| Main Metrics | MAE, RMSE, R^2 |

---

## Goal

Use one simple real dataset to practice the full supervised regression workflow end to end.
The point is not to squeeze out the best score. The point is to understand how a baseline behaves, what Linear Regression learns, which assumptions matter, and how residuals expose failure modes.

---

## What You Should Understand Before Writing Code

Write short answers to these first.

1. What does each row represent?
2. What exactly is the target, and what are its units?
3. What would a dumb predictor do here?
4. Why can RMSE and MAE disagree about model quality?
5. What patterns in a residual plot would tell you the linear model is missing structure?

If you cannot answer those yet, stop and inspect the data before building the model.

---

## Learning Questions

- What problem is this task solving?
- Why is a mean baseline necessary before training Linear Regression?
- Which features are likely to have roughly linear relationships with the target?
- Which features might break simple linear assumptions?
- What does R^2 say that MAE and RMSE do not?
- Where does the model make its largest errors?
- What would improve the model without jumping straight to a more complex model family?

---

## Dataset

### Source

- Dataset name: California Housing
- Access method: `sklearn.datasets.fetch_california_housing`
- Local cache used in this repo: `data/raw/sklearn_cache/cal_housing_py3.pkz`
- Primary reference: scikit-learn dataset loader docs
- Original source lineage: 1990 U.S. Census data prepared by Pace and Barry and distributed via StatLib
- Task dataset card: [dataset_card.md](dataset_card.md)

### Confirmed Shape

- Rows: 20,640
- Feature columns: 8
- Full frame columns including target: 9
- Target column: `MedHouseVal`
- Missing values in cached frame: none

### Feature List

- `MedInc`
- `HouseAge`
- `AveRooms`
- `AveBedrms`
- `Population`
- `AveOccup`
- `Latitude`
- `Longitude`

### What To Notice

- This is a clean starter regression dataset, but it is not a perfect linear world.
- Location is likely carrying nonlinear structure that a plain linear model cannot express well.
- The target is capped in the source data, so large-value prediction behavior deserves attention in error analysis.

---

## Recommended Workflow

Treat this as a guided lab. Do the stages in order and write down what you observe at each step.

### Stage 1 - Inspect the Problem

Before coding the model, answer:

- What is the prediction target?
- Is lower error always better in the same way for MAE and RMSE?
- What would a business or user actually care about if this were a real pricing system?

Deliverable for yourself:

- 3-5 bullet notes in the notebook or README scratch area.

### Stage 2 - Load and Inspect the Data

Tasks:

- Load the dataset as a DataFrame.
- Print shape, dtypes, column names, and target summary.
- Check whether any feature distributions look skewed or suspicious.
- Look at a few raw rows before any modeling.

Questions to answer:

- Which columns look like counts, ratios, or geographic coordinates?
- Which features may need extra interpretation before modeling?

### Stage 3 - Do Minimal EDA

Tasks:

- Plot the target distribution.
- Compute summary statistics.
- Check pairwise correlations carefully, without over-trusting them.
- Create at least one scatter plot between a likely useful feature and the target.

Questions to answer:

- Which feature seems most useful at first glance?
- Which feature seems noisy or misleading?
- Do you see signs that a linear fit may underperform in certain regions?

### Stage 4 - Define the Baseline

Tasks:

- Build a predictor that always outputs the training-set mean target value.
- Evaluate it on the test split.

Questions to answer:

- Why must the baseline use the training mean, not the full-dataset mean?
- What does baseline RMSE represent in plain language?

### Stage 5 - Train Linear Regression

Tasks:

- Split the data into train and test sets.
- Train a plain Linear Regression model.
- Record coefficients and intercept.

Questions to answer:

- Which coefficient signs make sense?
- Which ones are surprising?
- Does coefficient magnitude mean the same thing before and after scaling?

### Stage 6 - Evaluate Properly

Tasks:

- Compare baseline and model on MAE, RMSE, and R^2.
- Save the metrics to `outputs/metrics.json`.
- Save predictions if you want deeper error analysis later.

Questions to answer:

- Did the model clearly beat the baseline?
- Did all metrics improve together?
- If MAE looks decent but RMSE is worse than expected, what does that suggest?

### Stage 7 - Residual Analysis

Tasks:

- Plot predicted vs actual.
- Plot residuals vs predicted values.
- Inspect a few largest-error examples.

Questions to answer:

- Are residuals centered around zero?
- Do errors grow with price?
- Is there visible curvature or structure that the linear model cannot capture?

### Stage 8 - Write the Learning Summary

Your final report must answer:

1. What did the model learn?
2. Where did it fail?
3. What specific change would you try next, and why?

Do not end with "try a better model" without naming what weakness that next model would address.

---

## Suggested File-by-File Work

- `notebook.ipynb`: EDA, scratch analysis, visualizations, interpretation notes
- `train.py`: final repeatable training path once you are ready to move from notebook exploration
- `evaluate.py`: reusable metric computation and artifact writing once you want a cleaner workflow
- `report.md`: final explanation of findings
- `outputs/plots/`: saved figures
- `outputs/metrics.json`: final machine-readable metrics

---

## Evaluation Plan

| Metric | Why It Matters |
|---|---|
| MAE | Easy to interpret as average absolute error in target units |
| RMSE | Penalizes large misses more strongly than MAE |
| R^2 | Shows variance explained relative to a mean baseline |

Validation strategy:

- Split: standard train/test split
- Suggested first pass: `random_state=42`
- Optional extension later: cross-validation after the first clean baseline comparison

---

## Checklist

- [x] Normalize task folder to `tasks/001_linear_regression_california_housing/`
- [x] Cache the dataset locally through the scikit-learn loader
- [x] Create task README and dataset card
- [ ] Load dataset manually and inspect raw rows
- [ ] Write down the problem statement in your own words
- [ ] Summarize target distribution and feature roles
- [ ] Build a train/test split
- [ ] Implement mean baseline
- [ ] Implement Linear Regression
- [ ] Compare MAE, RMSE, and R^2
- [ ] Save `outputs/metrics.json`
- [ ] Save plots under `outputs/plots/`
- [ ] Write `report.md`
- [ ] Update `EXPERIMENT_LOG.md` with real run results
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

- the dataset is documented clearly
- the baseline is implemented and evaluated
- Linear Regression is implemented and evaluated
- metrics are saved and explained
- residual analysis is included
- `report.md` answers what the model learned, where it failed, and what would improve it
- global trackers are updated

---

## Notes

- Do not jump to Ridge/Lasso here unless you are explicitly comparing why plain Linear Regression struggles.
- If you find yourself feature engineering heavily, write down why. That observation is part of the learning.
- Keep the first version simple enough that you can explain every line and every metric.
