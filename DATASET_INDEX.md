# Dataset Index

This file tracks datasets that have been selected for actual tasks in the repo.

Do not add datasets here just because they are interesting. Add a dataset only when it is introduced into a task or explicitly selected for an upcoming task.

---

## Update Rules

1. Append new datasets when they are first used or selected.
2. Keep dataset names stable.
3. Link every dataset to one or more task IDs.
4. Include source, license/usage notes, target, and local path/download method.
5. Do not commit large raw datasets unless they are tiny and license-safe.
6. If a dataset changes location or preprocessing status, update the same row instead of creating duplicates.
7. If the dataset has a task-level dataset card, link it in the `Dataset Card` column.

---

## Dataset Table

| Dataset | Source | Data Type | Task Type | Target | Used In | Local Path / Access | License / Usage Notes | Dataset Card | Status |
|---|---|---|---|---|---|---|---|---|---|
| California Housing | scikit-learn `fetch_california_housing` | Tabular | Regression | Median house value | 001 | Loaded through scikit-learn cache | Use through scikit-learn; document source in Task 001 | `tasks/001_linear_regression_california_housing/dataset_card.md` | PLANNED |

---

## Dataset Status Values

| Status | Meaning |
|---|---|
| PLANNED | Selected for a task but not yet used |
| ACTIVE | Currently used in an active task |
| USED | Used in at least one completed task |
| DEPRECATED | No longer recommended for future tasks |
| BLOCKED | Dataset has access, licensing, quality, or download issues |

---

## Dataset Addition Template

```md
| Dataset Name | Source | Data Type | Task Type | Target | Task ID | Path or access method | License / usage note | `path/to/dataset_card.md` | PLANNED |
```
