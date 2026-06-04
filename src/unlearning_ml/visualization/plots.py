"""Reusable plotting helpers."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def save_current_plot(path: str | Path, dpi: int = 150) -> Path:
    """Save the current matplotlib figure and close it."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close()
    return output_path
