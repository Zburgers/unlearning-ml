# Dataset Card: California Housing

## Dataset Metadata

| Field | Value |
|---|---|
| Dataset Name | California Housing |
| Used In Task(s) | 001 |
| Source | `sklearn.datasets.fetch_california_housing` |
| License | Use through scikit-learn distribution; original lineage should be cited in task notes |
| Data Type | Tabular |
| Task Type | Regression |
| Target | `MedHouseVal` |
| Download Method | Library fetch through scikit-learn |
| Local Path | `data/raw/sklearn_cache/cal_housing_py3.pkz` |

---

## Description

This dataset contains demographic, geographic, and housing summary variables for California districts.
It is a strong first regression dataset because it is small enough to inspect directly, clean enough to start quickly, and rich enough to show where a linear model falls short.

---

## Schema

| Column | Type | Description | Used? | Notes |
|---|---|---|---|---|
| `MedInc` | numeric | Median income in block group | Yes | Often strongly predictive |
| `HouseAge` | numeric | Median house age in block group | Yes | May have nonlinear effects |
| `AveRooms` | numeric | Average rooms per household | Yes | Ratio feature |
| `AveBedrms` | numeric | Average bedrooms per household | Yes | Ratio feature |
| `Population` | numeric | Block group population | Yes | Scale-sensitive |
| `AveOccup` | numeric | Average household occupancy | Yes | Can contain outlier behavior |
| `Latitude` | numeric | Latitude | Yes | Captures geography |
| `Longitude` | numeric | Longitude | Yes | Captures geography |
| `MedHouseVal` | numeric | Median house value | Yes | Regression target |

---

## Size

| Field | Value |
|---|---|
| Rows | 20,640 |
| Columns | 9 including target |
| Classes | N/A |
| Missing Values | None in the cached scikit-learn frame |
| Duplicate Rows | TBD by task work |

---

## Target Variable

- Target name: `MedHouseVal`
- Target type: continuous numeric
- Target distribution: inspect directly during EDA
- Notes: the scikit-learn dataset documentation reports the target range as roughly `0.15` to `5.0`

---

## Data Quality Notes

- Missing values: none in the cached frame
- Outliers: likely in occupancy, rooms, and population-derived ratios
- Class imbalance: not applicable
- Duplicates: not yet checked in task work
- Noisy labels: possible due to aggregation and target capping
- Bias risks: location and socioeconomic patterns may dominate prediction behavior

---

## Leakage Risks

List anything that could accidentally leak target information.

- Do not compute preprocessing statistics on the full dataset before the train/test split.
- Do not use the full-dataset mean as the baseline target.
- Do not tune decisions directly on the test set.

---

## Preprocessing Plan

- Start with the raw scikit-learn frame.
- Split train and test first.
- Build the mean baseline from the training target only.
- Add scaling only if you can explain why you want it.
- Record every transformation in the task report.

---

## Usage Notes

- Keep the cached dataset out of Git.
- Prefer the documented scikit-learn fetch path over manually downloading a duplicate CSV.
- Update `DATASET_INDEX.md` if the dataset status changes again.
