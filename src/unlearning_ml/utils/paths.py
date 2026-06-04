"""Path helpers for repository-level scripts and tasks."""

from __future__ import annotations

from pathlib import Path


def find_repo_root(start: Path | None = None) -> Path:
    """Find the repository root by walking upward until key project files are found."""
    current = (start or Path.cwd()).resolve()

    for path in [current, *current.parents]:
        if (path / "README.md").exists() and (path / "ROADMAP.md").exists():
            return path

    msg = "Could not find repo root containing README.md and ROADMAP.md"
    raise FileNotFoundError(msg)


def project_path(*parts: str) -> Path:
    """Return an absolute path inside the repository."""
    return find_repo_root().joinpath(*parts)


def ensure_dir(path: str | Path) -> Path:
    """Create a directory if it does not exist and return it as a Path."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory
