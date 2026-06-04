from __future__ import annotations

import pandas as pd

from unlearning_ml.data.validation import assert_target_exists, dataframe_summary


def test_dataframe_summary_counts_rows_columns_and_missing_values() -> None:
    df = pd.DataFrame({"feature": [1, 2, None], "target": [10, 20, 30]})

    summary = dataframe_summary(df)

    assert summary["rows"] == 3
    assert summary["columns"] == 2
    assert summary["missing_values"] == 1
    assert summary["duplicate_rows"] == 0
    assert summary["column_names"] == ["feature", "target"]


def test_assert_target_exists_passes_for_existing_target() -> None:
    df = pd.DataFrame({"target": [1, 2, 3]})

    assert_target_exists(df, "target")
