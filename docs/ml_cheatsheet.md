# ML Cheatsheet

A compact reference for choosing models, data splits, and evaluation approaches across the repo.

---

## Supervised Learning

Use supervised learning when the dataset has labels or targets.

| Task Type | Goal | Example Models | Common Metrics |
|---|---|---|---|
| Regression | Predict a number | Linear Regression, Random Forest, XGBoost, MLP | MAE, RMSE, R² |
| Binary Classification | Predict one of two classes | Logistic Regression, SVM, Random Forest | Accuracy, Precision, Recall, F1, ROC-AUC |
| Multiclass Classification | Predict one of many classes | Logistic Regression, Random Forest, CNN, Transformer | Accuracy, Macro F1, Confusion Matrix |
| Multi-label Classification | Predict multiple labels per sample | Logistic Regression, Neural Networks | Micro/Macro F1, Precision@K |

---

## Unsupervised Learning

Use unsupervised learning when labels are missing or the goal is structure discovery.

| Task Type | Goal | Example Models | Common Metrics / Checks |
|---|---|---|---|
| Clustering | Group similar samples | K-Means, DBSCAN, GMM | Silhouette, cluster inspection |
| Dimensionality Reduction | Compress or visualize features | PCA, t-SNE, UMAP | Explained variance, visualization |
| Anomaly Detection | Find unusual samples | Isolation Forest, LOF, Autoencoder | Manual review, precision/recall if labels exist |

---

## Model Selection Heuristics

| Situation | Start With |
|---|---|
| Simple tabular regression | Mean baseline + Linear Regression |
| Simple binary classification | Majority baseline + Logistic Regression |
| Nonlinear tabular patterns | Decision Tree / Random Forest |
| Strong tabular benchmark | Gradient Boosting / XGBoost / LightGBM |
| High-dimensional sparse text | TF-IDF + Logistic Regression / Naive Bayes |
| Images | CNN / transfer learning |
| Audio | MFCC baseline, then spectrogram CNN |
| Time-series forecasting | Naive forecast, lag features, walk-forward validation |
| Recommendations | Popularity baseline, collaborative filtering |

---

## Baseline Rule

Always build a dumb baseline first.

Examples:

- Regression: predict training target mean
- Classification: predict majority class
- Forecasting: predict previous value
- Recommendation: recommend most popular items
- Ranking: random or popularity baseline

A serious model is only impressive if it beats a relevant baseline.

---

## Common Failure Modes

- Data leakage
- Bad train/test split
- Imbalanced target
- Overfitting
- Underfitting
- Wrong metric
- Target encoding leakage
- Duplicate rows across splits
- Time leakage in forecasting
- Evaluating on the validation set too many times
- Confusing correlation with causation

---

## Standard ML Workflow

```txt
Understand problem
↓
Load data
↓
Explore data
↓
Define metric
↓
Split data correctly
↓
Build baseline
↓
Train model
↓
Evaluate model
↓
Analyze errors
↓
Write report
↓
Update trackers
```
