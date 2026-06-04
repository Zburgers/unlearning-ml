"""Small data validation helpers."""

from __future__ import annotations

import pandas as pd


def dataframe_summary(df: pd.DataFrame) -> dict[str, object]:
    """Return a compact summary for a pandas DataFrame."""
    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "column_names": list(df.columns),
    }


def assert_target_exists(df: pd.DataFrame, target: str) -> None:
    """Raise a clear error if a target column is missing."""
    if target not in df.columns:
        msg = f"Target column '{target}' not found in dataframe."
        raise ValueError(msg)
