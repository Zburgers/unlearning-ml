"""Reusable feature engineering placeholders.

Keep task-specific feature engineering inside task folders until a pattern is reused.
"""

from __future__ import annotations

import pandas as pd


def select_numeric_features(df: pd.DataFrame) -> pd.DataFrame:
    """Return only numeric columns from a DataFrame."""
    return df.select_dtypes(include="number").copy()
