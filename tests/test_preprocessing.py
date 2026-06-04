from __future__ import annotations

import pandas as pd

from unlearning_ml.data.preprocessing import make_train_test_split
from unlearning_ml.features.feature_engineering import select_numeric_features


def test_make_train_test_split_returns_expected_sizes() -> None:
    X = pd.DataFrame({"x": range(10)})
    y = pd.Series(range(10))

    X_train, X_test, y_train, y_test = make_train_test_split(X, y, test_size=0.2, random_state=42)

    assert len(X_train) == 8
    assert len(X_test) == 2
    assert len(y_train) == 8
    assert len(y_test) == 2


def test_select_numeric_features_keeps_only_numeric_columns() -> None:
    df = pd.DataFrame({"num": [1, 2], "text": ["a", "b"]})

    result = select_numeric_features(df)

    assert list(result.columns) == ["num"]
