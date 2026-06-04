"""Dataset loading helpers.

Task-specific loaders can live inside task folders. This module is only for small,
reusable loading utilities used across multiple tasks.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path, **kwargs)


def load_parquet(path: str | Path, **kwargs) -> pd.DataFrame:
    """Load a Parquet file into a pandas DataFrame."""
    return pd.read_parquet(path, **kwargs)
