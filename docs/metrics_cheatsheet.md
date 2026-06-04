# Metrics Cheatsheet

Use this file to choose metrics that match the task.

Do not report metrics without explaining what they mean.

---

## Regression Metrics

| Metric | Meaning | Use When | Watch Out |
|---|---|---|---|
| MAE | Average absolute error | You want understandable error size | Treats all errors linearly |
| MSE | Average squared error | You want to penalize large errors | Harder to interpret due to squared units |
| RMSE | Square root of MSE | You want error in target units with large-error penalty | Sensitive to outliers |
| R² | Variance explained compared to mean baseline | You want relative explanatory power | Can be misleading alone |
| MAPE | Average percent error | Forecasting/business contexts | Breaks near zero targets |

Recommended default for regression:

```txt
MAE + RMSE + R²
```

---

## Classification Metrics

| Metric | Meaning | Use When | Watch Out |
|---|---|---|---|
| Accuracy | Fraction correct | Balanced classes | Misleading on imbalanced data |
| Precision | Of predicted positives, how many are correct | False positives are costly | Ignores missed positives |
| Recall | Of actual positives, how many were found | False negatives are costly | Can increase with many false positives |
| F1 | Harmonic mean of precision and recall | Need balance between precision/recall | Hides threshold behavior |
| ROC-AUC | Ranking quality across thresholds | Binary classification | Can look good on imbalanced data |
| PR-AUC | Precision-recall tradeoff | Imbalanced classification | More informative for rare positives |
| Confusion Matrix | Error breakdown | Any classification task | Needs interpretation |

Recommended default for binary classification:

```txt
Accuracy + Precision + Recall + F1 + ROC-AUC + Confusion Matrix
```

For imbalanced classification:

```txt
Precision + Recall + F1 + PR-AUC + Confusion Matrix
```

---

## Clustering Metrics

| Metric | Meaning | Watch Out |
|---|---|---|
| Silhouette Score | How separated clusters are | Can favor simple blob-like clusters |
| Inertia | Within-cluster distance for K-Means | Always decreases as K increases |
| Davies-Bouldin | Cluster separation/compactness | Hard to interpret alone |

Always pair clustering metrics with visual inspection and interpretation.

---

## Forecasting Metrics

| Metric | Meaning | Watch Out |
|---|---|---|
| MAE | Average forecast error | Good default |
| RMSE | Penalizes large forecast errors | Sensitive to spikes |
| MAPE | Percent error | Bad when actual values are near zero |
| sMAPE | Symmetric percent error | Still can be tricky to interpret |

Always compare forecasting models against a naive forecast.

---

## Ranking / Recommender Metrics

| Metric | Meaning |
|---|---|
| Precision@K | Fraction of top-K recommendations that are relevant |
| Recall@K | Fraction of relevant items found in top-K |
| MAP | Mean average precision across users/queries |
| NDCG | Rewards relevant items appearing higher in ranking |

---

## Metric Selection Rule

Before training, write down:

```txt
Primary metric:
Why this metric:
Secondary metrics:
Failure mode this metric misses:
```

If the metric does not match the real goal, the model result is not meaningful.
