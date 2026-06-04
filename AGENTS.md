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

# Agent Operating Manual

This file explains how humans and AI agents should work inside this repository without corrupting project state.

The repo is designed around scoped updates. Each file has a specific job. Do not dump all information into one file.

---

## File Responsibilities

| File | Purpose | Update Style |
|---|---|---|
| `ROADMAP.md` | Long-term learning map and phase-level plan | Rare edits only |
| `TASKS.md` | Global task state, active task checklist, backlog, blockers | Update when task state changes |
| `PROGRESS.md` | Daily/session progress notes and decisions | Append newest entry at top |
| `EXPERIMENT_LOG.md` | Compact experiment result rows | Append one row per meaningful run |
| `MODEL_INDEX.md` | Index of models covered across the repo | Append/update after task completion |
| `DATASET_INDEX.md` | Index of datasets used across the repo | Append/update when dataset is introduced |
| `templates/` | Reusable markdown templates | Edit only when improving workflow |
| `tasks/<task_id_slug>/README.md` | Task-specific plan and instructions | Update within that task scope |
| `tasks/<task_id_slug>/report.md` | Final task findings and learning summary | Update after experiments/results |
| `tasks/<task_id_slug>/outputs/metrics.json` | Machine-readable task metrics | Overwrite only for that task/run |

Do not duplicate full reports inside `TASKS.md`, `PROGRESS.md`, or `EXPERIMENT_LOG.md`.

---

## Scope Control Rules

When working on a task, agents must stay inside the requested scope.

### Active Task Scope

For normal task work, touch only:

```txt
TASKS.md
PROGRESS.md
EXPERIMENT_LOG.md
tasks/<active_task_slug>/
DATASET_INDEX.md, only if a new dataset is introduced
MODEL_INDEX.md, only if a model is completed or meaningfully used
```

Do not edit `ROADMAP.md` unless the user explicitly asks to change the long-term plan.

Do not edit unrelated task folders unless the user explicitly asks.

Do not renumber tasks.

Do not move tasks between phases unless the user explicitly asks or the current files clearly require correction.

### Template Scope

When changing workflow templates, touch only:

```txt
templates/
AGENTS.md, if workflow rules changed
PROGRESS.md, only if progress format changed
EXPERIMENT_LOG.md, only if experiment format changed
```

Do not rewrite completed task reports just because a template changed.

### Documentation Scope

When updating high-level documentation, touch only the relevant docs file unless a cross-reference must be updated.

Examples:

- Editing roadmap: `ROADMAP.md`
- Editing task state: `TASKS.md`
- Editing session progress: `PROGRESS.md`
- Editing result rows: `EXPERIMENT_LOG.md`
- Editing a task plan: `tasks/<task_id_slug>/README.md`
- Editing final findings: `tasks/<task_id_slug>/report.md`

---

# Task Tracker Operating Rules

`TASKS.md` is the global execution board for this repository.

It is designed for both humans and AI agents. Keep it readable, stable, and easy to update.

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
15. If a task is blocked, add or update the row in the `Blockers` section.
16. If a task is completed, add a compact summary to `Completed Tasks`.

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

# Progress Log Rules

`PROGRESS.md` is the session journal.

Use it to record what happened during a work session.

## Append Workflow

1. Add a new entry under `Progress Entries`.
2. Newest entries go at the top.
3. Use the template in `templates/progress_entry_template.md`.
4. Keep the entry short and useful.
5. Link task IDs and file paths.
6. Mention decisions and blockers.
7. Do not paste full experiment reports.
8. Do not paste large logs.

## When to Update PROGRESS.md

Update `PROGRESS.md` when:

- A task is started.
- A task changes status.
- A meaningful file scaffold is created.
- A decision is made.
- A blocker is discovered or resolved.
- A task is completed.

---

# Experiment Log Rules

`EXPERIMENT_LOG.md` is the compact experiment ledger.

Use it to compare runs across time without reading every notebook or report.

## Append Workflow

1. Add one row per meaningful experiment run.
2. Use the row format in `templates/experiment_log_row_template.md`.
3. Keep results compact.
4. Link to `metrics.json` or another artifact when available.
5. Mark invalid runs as invalid instead of deleting them.
6. Keep detailed interpretation inside the task `report.md`.

## When to Update EXPERIMENT_LOG.md

Update `EXPERIMENT_LOG.md` when:

- A baseline is run.
- A model is trained and evaluated.
- A hyperparameter or preprocessing variant is tested.
- A run is invalid but useful to remember.
- A best model changes.

---

# Dataset and Model Index Rules

## DATASET_INDEX.md

Update `DATASET_INDEX.md` when a dataset is first introduced.

Each dataset entry should include:

- Dataset name
- Source
- Data type
- Task type
- Used task IDs
- Target, if applicable
- License or usage notes
- Local path or download method

Do not add a dataset just because it is mentioned as a future idea. Add it when it is selected for a task.

## MODEL_INDEX.md

Update `MODEL_INDEX.md` when a model is meaningfully implemented, evaluated, or compared.

Each model entry should include:

- Model name
- Model family
- Task IDs where used
- Data types used on
- Main learning point
- Notes or limitations

Do not mark a model as covered until there is working code and at least one evaluation or analysis.

---

# Task Folder Rules

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
- `PROGRESS.md` is updated.
- `TASKS.md` is updated.

---

# Safe Update Sequences

Use these sequences to avoid partial or inconsistent tracking.

## Starting a Task

1. Read `ROADMAP.md`.
2. Read `TASKS.md`.
3. Identify the active `P0` task.
4. Create or update the task folder.
5. Update task status in `TASKS.md` from `TODO` to `IN_PROGRESS`.
6. Add a session entry to `PROGRESS.md`.

## Running an Experiment

1. Work inside the active task folder.
2. Save metrics/artifacts inside that task's `outputs/` folder.
3. Add one row to `EXPERIMENT_LOG.md`.
4. Add a short progress entry to `PROGRESS.md` if the result changes direction or status.
5. Update `TASKS.md` status if needed.

## Completing a Task

1. Finalize task `README.md`.
2. Finalize task `report.md`.
3. Confirm `outputs/metrics.json` exists.
4. Confirm `EXPERIMENT_LOG.md` has the main runs.
5. Update `MODEL_INDEX.md` for implemented models.
6. Update `DATASET_INDEX.md` for used datasets.
7. Mark the task `DONE` in `TASKS.md`.
8. Add a summary row to `Completed Tasks` in `TASKS.md`.
9. Add a completion entry to `PROGRESS.md`.
10. Set the next task as `P0` only when explicitly starting it.

## Adding a New Task

1. Check the highest existing task ID in `TASKS.md`.
2. Assign the next stable three-digit ID.
3. Add the task to the appropriate sprint or backlog table.
4. Add active task detail only if it becomes the current `P0` task.
5. Do not create a folder until the task is ready to start unless the user asks for scaffolding.

---

# Agent Behavior

When an AI agent works on this repo:

1. Read `ROADMAP.md` first.
2. Read `TASKS.md` second.
3. Read this `AGENTS.md` file third.
4. Identify the active `P0` task.
5. Work only on the active task unless explicitly asked otherwise.
6. Before creating a new task, check the latest task ID.
7. Do not overwrite existing task work without a clear reason.
8. Keep generated files small, clear, and reviewable.
9. Prefer incremental commits with clear messages.
10. If blocked, update the `Blockers` section in `TASKS.md` and add a `PROGRESS.md` note.
11. If a task is completed, update `Completed Tasks` in `TASKS.md` and add the result to `EXPERIMENT_LOG.md`.
12. Never silently change roadmap direction, task numbering, or completion criteria.

---

# Commit Message Style

Use direct, descriptive commit messages:

```txt
Seed Task 001 tracker
Initialize progress and experiment logs
Create Task 001 scaffold
Add Task 001 regression baseline
Add Task 001 evaluation report
Update experiment log for Task 001
Update dataset and model indexes for Task 001
```
