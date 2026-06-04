# Data Directory

This directory is for local datasets used by the repo.

Large raw datasets should usually stay out of Git. Prefer documented download scripts, library fetchers, or external dataset caches.

---

## Directory Structure

```txt
data/
├── raw/        # Original data exactly as downloaded, usually gitignored
├── interim/    # Temporary intermediate files, usually gitignored
├── processed/  # Cleaned/model-ready files, usually gitignored unless tiny
└── README.md   # Data handling rules
```

---

## Data Rules

1. Do not commit large datasets.
2. Do not commit private, sensitive, or licensed data unless explicitly allowed.
3. Keep raw data unchanged.
4. Save cleaned/transformed data under `data/processed/`.
5. Document every selected dataset in `DATASET_INDEX.md`.
6. Add a dataset card for task-specific datasets when useful.
7. Prefer reproducible dataset loading through code.
8. If data is generated synthetically, document the generation script and random seed.

---

## Recommended Access Pattern

For small built-in datasets:

```python
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
```

For manually downloaded datasets:

```txt
data/raw/<dataset_name>/
```

For processed datasets:

```txt
data/processed/<dataset_name>/
```

---

## Git Policy

The default policy is:

```txt
data/raw/**        ignored
data/interim/**    ignored
data/processed/**  ignored unless intentionally allowed
```

Use `.gitkeep` files if empty directories need to be preserved.

---

## Task 001 Dataset

Task 001 uses the California Housing dataset loaded through scikit-learn. It does not require manually committing raw data.
