"""Experiment runner placeholder.

Task-specific experiments should usually run from the task folder. This file can
later become a common CLI if repeated patterns emerge.
"""

from __future__ import annotations


def main() -> None:
    """Print guidance for running experiments."""
    print("Run experiments from the active task folder.")
    print("Save metrics to outputs/metrics.json and append results to EXPERIMENT_LOG.md.")


if __name__ == "__main__":
    main()
