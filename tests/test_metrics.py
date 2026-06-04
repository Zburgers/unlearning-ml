from __future__ import annotations

import pytest

from unlearning_ml.evaluation.classification import binary_classification_metrics
from unlearning_ml.evaluation.regression import regression_metrics


def test_regression_metrics_returns_expected_keys() -> None:
    metrics = regression_metrics([1.0, 2.0, 3.0], [1.0, 2.5, 2.5])

    assert set(metrics) == {"mae", "mse", "rmse", "r2"}
    assert metrics["mae"] >= 0
    assert metrics["rmse"] >= 0


def test_binary_classification_metrics_returns_expected_keys() -> None:
    metrics = binary_classification_metrics([0, 1, 1, 0], [0, 1, 0, 0])

    assert set(metrics) == {"accuracy", "precision", "recall", "f1"}
    assert metrics["accuracy"] == pytest.approx(0.75)
