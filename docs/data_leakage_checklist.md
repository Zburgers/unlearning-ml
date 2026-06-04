# Data Split and Evaluation Checklist

Use this checklist before trusting model results.

The main goal is to ensure the model is evaluated on data it did not learn from directly or indirectly.

---

## General Checks

- [ ] Was the train/test split created before fitting preprocessing steps?
- [ ] Were scalers fit only on training data?
- [ ] Were imputers fit only on training data?
- [ ] Were encoders fit only on training data?
- [ ] Were feature selection methods fit only on training data?
- [ ] Are duplicate rows kept out of both train and test at the same time?
- [ ] Does any feature directly contain the target?
- [ ] Does any feature contain future information?
- [ ] Was the test set kept separate from tuning?
- [ ] Were repeated experiments not optimized against the test set?

---

## Tabular Checks

- [ ] Are IDs, timestamps, or post-outcome fields accidentally predictive?
- [ ] Are aggregated features computed using training data only?
- [ ] Are target encodings computed after splitting?
- [ ] Are duplicated customers/users/entities grouped correctly?
- [ ] Is a group-based split needed?

---

## Time-Series Checks

- [ ] Is the split time-based instead of random?
- [ ] Are lag features only using past values?
- [ ] Are rolling windows shifted correctly?
- [ ] Are future covariates genuinely known at prediction time?
- [ ] Is walk-forward validation used when appropriate?

---

## Text Checks

- [ ] Are near-duplicate documents kept in the same split?
- [ ] Are labels excluded from filenames, metadata, or text fields?
- [ ] Is the vectorizer fitted only on training data?
- [ ] Are documents from the same source/entity grouped correctly?

---

## Image and Audio Checks

- [ ] Are augmented versions of the same sample kept in the same split?
- [ ] Are files from the same subject or scene grouped correctly?
- [ ] Are filenames or folder names excluded from model features?
- [ ] Are preprocessing statistics computed only from training data?

---

## Safe scikit-learn Pattern

Prefer pipelines for preprocessing and modeling:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression()),
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

---

## Result Trust Rule

If the evaluation setup is questionable, mark the experiment as invalid in `EXPERIMENT_LOG.md` until checked.

Do not delete the run. Keep it and explain why it is invalid.
