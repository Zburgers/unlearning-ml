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

## Required Agent Startup Sequence

Whenever the user asks an agent to work in this repo, update the repo, push to GitHub, push to main, continue the learning repo, or work on "unlearning ML", the agent must do this first:

1. Read `README.md` for project purpose.
2. Read `ROADMAP.md` for long-term direction.
3. Read `TASKS.md` for current state and active task.
4. Read `AGENTS.md` for operating rules.
5. Identify the active `P0` task.
6. Determine whether the request is:
   - task-scoped work
   - tracker/documentation work
   - template/workflow work
   - repo hygiene work
   - experiment/model work
   - dataset work
7. Touch only the files required for that scope.
8. Update trackers before considering the work complete.

Do not start coding or editing random files before checking the tracker state.

---

## File Responsibilities

| File | Purpose | Update Style |
|---|---|---|
| `README.md` | Public project overview | Rare edits when project positioning changes |
| `ROADMAP.md` | Long-term learning map and phase-level plan | Rare edits only |
| `TASKS.md` | Global task state, active task checklist, backlog, blockers | Update when task state changes |
| `PROGRESS.md` | Daily/session progress notes and decisions | Append newest entry at top |
| `EXPERIMENT_LOG.md` | Compact experiment result rows | Append one row per meaningful run |
| `MODEL_INDEX.md` | Index of models covered across the repo | Append/update after model use or task completion |
| `DATASET_INDEX.md` | Index of datasets used across the repo | Append/update when dataset is introduced |
| `NOTES.md` | Durable cross-task notes | Append only repo-level observations |
| `docs/` | General references and reusable guidance | Edit only when improving global guidance |
| `templates/` | Reusable markdown templates | Edit only when improving workflow |
| `src/unlearning_ml/` | Reusable code utilities | Add only reusable, task-agnostic helpers |
| `scripts/` | Repo-level helper scripts | Add only reusable automation |
| `tests/` | Tests for reusable code | Update when `src/` helpers change |
| `tasks/<task_id_slug>/README.md` | Task-specific plan and instructions | Update within that task scope |
| `tasks/<task_id_slug>/report.md` | Final task findings and learning summary | Update after experiments/results |
| `tasks/<task_id_slug>/outputs/metrics.json` | Machine-readable task metrics | Overwrite only for that task/run |

Do not duplicate full reports inside `TASKS.md`, `PROGRESS.md`, or `EXPERIMENT_LOG.md`.

---

## Scope Decision Rules

### If the user says: "work on Task XXX"

Scope is task-specific.

Allowed files:

```txt
TASKS.md
PROGRESS.md
EXPERIMENT_LOG.md
DATASET_INDEX.md, if a dataset is introduced or status changes
MODEL_INDEX.md, if a model is implemented or status changes
tasks/<task_id_slug>/
```

Do not touch unrelated task folders. Do not rewrite global roadmap or templates unless explicitly asked.

### If the user says: "update this and push to main" or "push this to unlearning/github/main"

Agent must infer the smallest safe scope from the changed work.

Before committing/pushing, check:

```txt
1. Did task status change? Update TASKS.md.
2. Was a session completed? Append PROGRESS.md.
3. Was a model run evaluated? Append EXPERIMENT_LOG.md.
4. Was a dataset introduced? Update DATASET_INDEX.md.
5. Was a model implemented/evaluated? Update MODEL_INDEX.md.
6. Was reusable code changed? Update or add tests.
7. Was workflow changed? Update AGENTS.md and templates if needed.
8. Was a task completed? Update task report, TASKS.md, PROGRESS.md, EXPERIMENT_LOG.md, MODEL_INDEX.md, DATASET_INDEX.md.
```

Only then commit and push.

### If the user says: "repo hygiene", "full pass", or "check leftovers"

Scope is global documentation/config/template hygiene.

Allowed files:

```txt
README.md, only if overview is stale
ROADMAP.md, only if long-term plan is stale
TASKS.md
PROGRESS.md
EXPERIMENT_LOG.md
DATASET_INDEX.md
MODEL_INDEX.md
NOTES.md
docs/
templates/
AGENTS.md
requirements.txt
pyproject.toml
.gitignore
src/, only for task-agnostic reusable utilities
scripts/, only for repo-level helpers
tests/, only for reusable utility tests
```

Do not edit task-specific README/report files during repo hygiene unless explicitly asked.

### If the user says: "add a dataset"

Update:

```txt
DATASET_INDEX.md
data/README.md, only if data handling rules change
tasks/<active_task_slug>/dataset_card.md, if task-specific
PROGRESS.md
TASKS.md, if the active task dataset/status changed
```

Do not commit large data files by default.

### If the user says: "add a model" or "try this model"

Update:

```txt
tasks/<active_task_slug>/ code/notebook/report as needed
EXPERIMENT_LOG.md, after evaluation
MODEL_INDEX.md, after meaningful implementation/evaluation
PROGRESS.md
TASKS.md, if status changes
```

Do not mark the model as `COVERED` until it has working code, metrics, and documentation.

### If the user says: "complete the task"

Run the task completion workflow. Do not mark `DONE` unless all required artifacts exist.

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
- A repo hygiene pass changes global structure.

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

Update `DATASET_INDEX.md` when a dataset is first introduced or its status changes.

Each dataset entry should include:

- Dataset name
- Source
- Data type
- Task type
- Used task IDs
- Target, if applicable
- License or usage notes
- Local path or download method
- Dataset card path, if available
- Status

Do not add a dataset just because it is mentioned as a future idea. Add it when it is selected for a task.

## MODEL_INDEX.md

Update `MODEL_INDEX.md` when a model is meaningfully implemented, evaluated, or compared.

Each model entry should include:

- Model name
- Model family
- Task IDs where used
- Data types used on
- Task types
- Status
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

1. Read `README.md`, `ROADMAP.md`, `TASKS.md`, and `AGENTS.md`.
2. Identify the active `P0` task.
3. Create or update the task folder.
4. Update task status in `TASKS.md` from `TODO` to `IN_PROGRESS`.
5. Add a session entry to `PROGRESS.md`.
6. Update dataset/model indexes only if new selections were made.

## Running an Experiment

1. Work inside the active task folder.
2. Save metrics/artifacts inside that task's `outputs/` folder.
3. Add one row to `EXPERIMENT_LOG.md`.
4. Add a short progress entry to `PROGRESS.md` if the result changes direction or status.
5. Update `TASKS.md` status if needed.
6. Update `MODEL_INDEX.md` if a model became meaningfully evaluated.

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

## Repo Hygiene Pass

1. Inspect global files and templates for empty placeholders.
2. Fill only global docs/config/templates/reusable utilities.
3. Do not touch task-specific README/report files unless requested.
4. Update `PROGRESS.md` with a hygiene pass entry.
5. Update `TASKS.md` only if tracker state changed.
6. Keep changes small and explainable.

## Commit and Push Workflow

Before committing:

1. Review changed files.
2. Confirm changes match the requested scope.
3. Confirm tracker files are updated if task state changed.
4. Confirm experiment logs are updated if metrics were produced.
5. Confirm dataset/model indexes are updated if relevant.
6. Run or describe relevant tests/checks where possible.
7. Use a direct commit message.
8. Push to `main` only if the user asked for GitHub/main/unlearning repo updates or the context clearly implies it.

Commit message examples:

```txt
Initialize global repo documentation
Create Task 001 scaffold
Add Task 001 regression baseline
Update experiment log for Task 001
Complete Task 001 regression report
```

---

# Agent Behavior

When an AI agent works on this repo:

1. Read `README.md`, `ROADMAP.md`, `TASKS.md`, and `AGENTS.md` first.
2. Identify the active `P0` task.
3. Decide the scope using the request and the rules above.
4. Work only inside that scope unless explicitly asked otherwise.
5. Before creating a new task, check the latest task ID.
6. Do not overwrite existing task work without a clear reason.
7. Keep generated files small, clear, and reviewable.
8. Prefer incremental commits with clear messages.
9. If blocked, update the `Blockers` section in `TASKS.md` and add a `PROGRESS.md` note.
10. If a task is completed, update `Completed Tasks` in `TASKS.md` and add the result to `EXPERIMENT_LOG.md`.
11. Never silently change roadmap direction, task numbering, or completion criteria.
12. Never silently commit large raw datasets or model binaries.
13. When unsure, choose the smallest safe file scope and document the decision in `PROGRESS.md`.
