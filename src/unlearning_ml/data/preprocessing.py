"""Reusable preprocessing helpers."""

from __future__ import annotations

from sklearn.model_selection import train_test_split


def make_train_test_split(X, y, test_size: float = 0.2, random_state: int = 42):
    """Create a reproducible train/test split.

    Keep task-specific split logic inside task folders when special handling is needed.
    For time-series tasks, do not use this helper.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
