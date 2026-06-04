"""Regression evaluation helpers."""

from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_metrics(y_true: Any, y_pred: Any) -> dict[str, float]:
    """Return standard regression metrics.

    Metrics returned:
    - MAE
    - MSE
    - RMSE
    - R2
    """
    mse = mean_squared_error(y_true, y_pred)
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "mse": float(mse),
        "rmse": float(np.sqrt(mse)),
        "r2": float(r2_score(y_true, y_pred)),
    }
