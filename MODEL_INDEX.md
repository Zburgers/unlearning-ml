# Model Index

This file tracks models that are planned, active, or covered across the repo.

A model is considered **covered** only when it has working code, metrics, and at least one analysis/report entry.

---

## Update Rules

1. Add a model when it is selected for a task or meaningfully implemented.
2. Do not mark a model as `COVERED` until it has been evaluated.
3. Link every model to one or more task IDs.
4. Keep notes short; put full analysis in task reports.
5. Update the same row when a model is reused in future tasks.
6. Use the model family names consistently.

---

## Model Table

| Model | Family | Used In | Data Types | Task Types | Status | Main Learning Point | Notes |
|---|---|---|---|---|---|---|---|
| Mean Baseline | Baseline | 001 | Tabular | Regression | PLANNED | Establishes a dumb comparison point before Linear Regression | Predicts the training target mean for all samples |
| Linear Regression | Linear Models | 001 | Tabular | Regression | PLANNED | Teaches linear relationships, coefficients, residuals, and regression metrics | First serious model in the repo |

---

## Model Status Values

| Status | Meaning |
|---|---|
| PLANNED | Selected for a task but not yet implemented |
| ACTIVE | Currently being implemented or evaluated |
| COVERED | Implemented, evaluated, and documented |
| NEEDS_REVIEW | Implemented but results or docs need verification |
| DEPRECATED | No longer recommended or replaced by a better workflow |

---

## Model Family Reference

| Family | Examples |
|---|---|
| Baseline | Mean predictor, majority-class predictor, random predictor |
| Linear Models | Linear Regression, Ridge, Lasso, ElasticNet, Logistic Regression |
| Tree-Based Models | Decision Tree, Random Forest, Extra Trees |
| Boosting Models | Gradient Boosting, XGBoost, LightGBM, CatBoost |
| Kernel / Distance Models | KNN, SVM, Kernel Ridge |
| Probabilistic Models | Naive Bayes, Bayesian Regression, HMMs, GMMs |
| Unsupervised Models | K-Means, DBSCAN, PCA, t-SNE, UMAP |
| Deep Learning | MLP, CNN, RNN, GRU, LSTM, Transformer, Autoencoder, U-Net |
| Recommenders / Ranking | Collaborative filtering, matrix factorization, learning-to-rank |

---

## Model Addition Template

```md
| Model Name | Family | Task ID | Data Type | Task Type | PLANNED | Main learning point | Short note |
```
