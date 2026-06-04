"""Reproducibility helpers."""

from __future__ import annotations

import os
import random

import numpy as np


def set_global_seed(seed: int = 42) -> int:
    """Set common Python and NumPy random seeds.

    Deep learning frameworks should be seeded inside task-specific code when used.
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    return seed
