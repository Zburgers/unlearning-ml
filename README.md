# Unlearning ML

A personal machine learning practice repository for rebuilding ML intuition from first principles across classical ML, deep learning, tabular data, text, images, audio, time-series, and probabilistic models.

## Why This Exists

This repo is my ML gym.  
The goal is not just to train models, but to understand:
- what problem each model is good for
- what assumptions it makes
- how it fails
- how to evaluate it properly
- how to explain the result

## Roadmap

1. ML setup and experiment hygiene
2. Linear models
3. Nonlinear classical ML
4. Unsupervised learning
5. Time-series and sequential modeling
6. Probabilistic models and HMMs
7. Deep learning basics
8. Computer vision
9. NLP
10. Audio and speech
11. Recommenders and ranking
12. Capstone projects

## Repository Structure

- `tasks/`: task-first workspaces with README, code, reports, and outputs per task
- `data/`: raw, interim, and processed datasets used by tasks
- `models/`: saved models and checkpoints
- `reports/`: figures, tables, and final reports
- `notebooks/`: learning notebooks by topic
- `src/`: reusable library code (data, features, models, evaluation, utils)
- `docs/`: documentation and references
- `templates/`: reusable task/report templates
- `scripts/`: helper scripts for data or experiments
- `tests/`: test suite for reusable code

## Current Sprint

See [TASKS.md](TASKS.md).

## Model Index

See [MODEL_INDEX.md](MODEL_INDEX.md).

## Dataset Index

See [DATASET_INDEX.md](DATASET_INDEX.md).

## Experiment Rules

Every task must include:
- dataset card
- baseline model
- at least one serious model
- metrics
- error analysis
- final report
- what I learned
