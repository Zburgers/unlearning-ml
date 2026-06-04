"""Classical ML model helpers.

Only add reusable factory/helper functions here after they are useful across tasks.
Task-specific model code should stay inside task folders.
"""

from __future__ import annotations

from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression


def mean_regression_baseline() -> DummyRegressor:
    """Return a regression baseline that predicts the training target mean."""
    return DummyRegressor(strategy="mean")


def linear_regression_model() -> LinearRegression:
    """Return a standard scikit-learn Linear Regression model."""
    return LinearRegression()
