"""Dataset download helper entry point.

This script is intentionally minimal for now. Add dataset-specific download logic only
when a task needs it and the dataset cannot be loaded through a library.
"""

from __future__ import annotations


def main() -> None:
    """Print guidance for dataset handling."""
    print("Use task-specific dataset loading unless a reusable downloader is needed.")
    print("Document selected datasets in DATASET_INDEX.md.")


if __name__ == "__main__":
    main()
