# Rules for the Repo

Follow these strictly:

1. Every task gets a README.
2. Every experiment gets a report.
3. Every model gets compared to a dumb baseline.
4. Every dataset gets a dataset card.
5. No unexplained metrics.
6. No notebook-only projects after Phase 1.
7. Every task must answer: what did the model learn, where did it fail, and what would improve it?
8. Keep raw data out of Git unless tiny and license-safe.
9. Save outputs as metrics.json, plots, and report.md.
10. Commit after each completed task.

---

# Task Tracker Operating Rules

`TASKS.md` is the global execution board for this repository.

It is designed for both humans and AI agents. Keep it readable, stable, and easy to update.

## File Responsibilities

Use the files this way:

| File | Purpose |
|---|---|
| `ROADMAP.md` | Long-term learning map and phase-level plan |
| `TASKS.md` | Global task state, active task checklist, backlog, blockers |
| `PROGRESS.md` | Daily or session-based progress notes |
| `EXPERIMENT_LOG.md` | Compact table of experiment results and metrics |
| `MODEL_INDEX.md` | Index of models covered across the repo |
| `DATASET_INDEX.md` | Index of datasets used across the repo |
| `tasks/<task_id_slug>/README.md` | Task-specific plan and instructions |
| `tasks/<task_id_slug>/report.md` | Final task findings and learning summary |
| `tasks/<task_id_slug>/outputs/metrics.json` | Machine-readable task metrics |

Do not duplicate full reports inside `TASKS.md`.

---

## TASKS.md Editing Rules

When editing `TASKS.md`:

1. Keep task IDs stable. Never renumber existing tasks.
2. Use three-digit task IDs: `001`, `002`, `003`.
3. Use snake_case slugs: `001_linear_regression_california_housing`.
4. Append new tasks instead of inserting and renumbering old ones.
5. Keep exactly one `P0` task unless there is a deliberate parallel-work reason.
6. Keep exactly one active task in `Tracker Metadata`.
7. Update `Last Updated` using `YYYY-MM-DD`.
8. Use only the approved status values.
9. Use only the approved priority values.
10. Keep the active task checklist practical and actionable.
11. Do not add long experiment notes, code explanations, or result narratives to `TASKS.md`.
12. Move detailed results to the task `report.md`.
13. Move metric rows to `EXPERIMENT_LOG.md`.
14. Move daily/session notes to `PROGRESS.md`.

---

## Approved Status Values

Use only these values:

| Status | Meaning |
|---|---|
| TODO | Planned but not started |
| IN_PROGRESS | Task folder/code exists and work has started |
| EXPERIMENTING | Models are being trained, evaluated, or compared |
| REPORTING | Results exist; README/report/log updates are pending |
| DONE | Task meets the definition of done |
| BLOCKED | Task cannot continue without a decision, dataset, dependency, or fix |
| NEEDS_REVIEW | Task is mostly complete but needs verification |

---

## Approved Priority Values

Use only these values:

| Priority | Meaning |
|---|---|
| P0 | Current active task |
| P1 | Start soon after active task |
| P2 | Planned backlog |
| P3 | Future/optional |

---

## Task Lifecycle

Tasks should move through this lifecycle:

```txt
TODO -> IN_PROGRESS -> EXPERIMENTING -> REPORTING -> DONE
```

Use `BLOCKED` only when the task genuinely cannot continue.

Use `NEEDS_REVIEW` when implementation is mostly complete but requires verification.

---

## Task Folder Rules

Every task folder should follow this structure:

```txt
tasks/<task_id_slug>/
├── README.md
├── notebook.ipynb
├── train.py
├── evaluate.py
├── report.md
└── outputs/
    ├── metrics.json
    ├── predictions.csv
    └── plots/
```

For early Phase 1 learning tasks, a notebook-only workflow is allowed if the task is still well documented.

After Phase 1, prefer script-backed experiments with notebooks used for exploration and explanation.

---

## Definition of Done for Any Task

A task can be marked `DONE` only when:

- The task folder exists.
- The task README explains the goal, dataset, models, metrics, and learning questions.
- A dumb baseline is included.
- At least one serious model is implemented.
- Metrics are saved and explained.
- Failure cases or errors are analyzed.
- `report.md` summarizes results and learning.
- `EXPERIMENT_LOG.md` is updated.
- `TASKS.md` is updated.

---

## Agent Behavior

When an AI agent works on this repo:

1. Read `ROADMAP.md` first.
2. Read `TASKS.md` second.
3. Identify the active `P0` task.
4. Work only on the active task unless explicitly asked otherwise.
5. Before creating a new task, check the latest task ID.
6. Do not overwrite existing task work without a clear reason.
7. Keep generated files small, clear, and reviewable.
8. Prefer incremental commits with clear messages.
9. If blocked, update the `Blockers` section in `TASKS.md`.
10. If a task is completed, update `Completed Tasks` in `TASKS.md` and add the result to `EXPERIMENT_LOG.md`.

---

## Commit Message Style

Use direct, descriptive commit messages:

```txt
Seed Task 001 tracker
Create Task 001 scaffold
Add Task 001 regression baseline
Add Task 001 evaluation report
Update experiment log for Task 001
```
