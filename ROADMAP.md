# Unlearning ML Roadmap

This roadmap is the operating plan for **Unlearning ML**: a personal machine learning practice repository for rebuilding ML intuition from fundamentals to advanced applied systems.

The goal is not to collect random notebooks.  
The goal is to build a structured ML gym where every task teaches a model family, a data type, an evaluation method, and a practical failure mode.

---

## Project Philosophy

Unlearning ML exists to relearn machine learning from the ground up by repeatedly doing real tasks.

Each task should answer:

1. What problem am I solving?
2. What data type am I working with?
3. What model family am I practicing?
4. What assumptions does the model make?
5. What baseline am I comparing against?
6. What metric actually matters?
7. Where does the model fail?
8. What would I try next?

This repo should become a fast revision system, a practical ML reference, and a portfolio-quality record of hands-on ML practice.

---

## Roadmap Overview

| Phase | Area | Main Goal | Status |
|---|---|---|---|
| Phase 0 | Setup and Experiment Hygiene | Build reusable repo workflow | TODO |
| Phase 1 | Linear Models | Relearn regression/classification foundations | TODO |
| Phase 2 | Nonlinear Classical ML | Trees, kernels, ensembles, boosting | TODO |
| Phase 3 | Unsupervised Learning | Clustering, PCA, anomaly detection | TODO |
| Phase 4 | Time-Series and Sequential Data | Forecasting and temporal validation | TODO |
| Phase 5 | Probabilistic Models and HMMs | Bayesian thinking, Naive Bayes, HMMs | TODO |
| Phase 6 | Deep Learning Basics | MLPs, tensors, optimization, regularization | TODO |
| Phase 7 | Computer Vision | CNNs, transfer learning, detection, segmentation | TODO |
| Phase 8 | NLP | TF-IDF, embeddings, sequence models, transformers | TODO |
| Phase 9 | Audio and Speech | MFCCs, spectrograms, audio classification | TODO |
| Phase 10 | Recommenders and Ranking | Similarity, matrix factorization, ranking metrics | TODO |
| Phase 11 | Capstones | End-to-end real-world ML systems | TODO |

---

# Phase 0 — Setup and Experiment Hygiene

## Goal

Create the foundation for clean, repeatable ML experiments.

This phase is complete only when the repo has reusable templates, documentation rules, metrics conventions, and a basic experiment workflow.

## Concepts

- Project structure
- Reproducibility
- Random seeds
- Train/validation/test splits
- Dataset cards
- Model cards
- Experiment reports
- Metrics logging
- Data leakage prevention
- Git hygiene for ML projects

## Deliverables

- `README.md`
- `ROADMAP.md`
- `TASKS.md`
- `MODEL_INDEX.md`
- `DATASET_INDEX.md`
- `EXPERIMENT_LOG.md`
- `docs/data_leakage_checklist.md`
- `docs/metrics_cheatsheet.md`
- `templates/task_README_template.md`
- `templates/experiment_report_template.md`
- `templates/model_card_template.md`
- `templates/dataset_card_template.md`

## Completion Criteria

- Every future task has a consistent folder structure.
- Every task has a README, notebook/script, report, and saved outputs.
- There is a clear rule for what counts as DONE.
- Raw datasets are not blindly committed to Git.
- Experiments can be reproduced from notes.

---

# Phase 1 — Linear Models and Basic Tabular ML

## Goal

Rebuild the foundation of supervised learning using simple, interpretable models.

Start with tabular data because it makes the full ML workflow visible: cleaning, encoding, scaling, splitting, training, evaluating, and interpreting.

## Models

- Mean/majority baseline
- Simple Linear Regression
- Multiple Linear Regression
- Polynomial Regression
- Ridge Regression
- Lasso Regression
- ElasticNet
- Logistic Regression

## Concepts

- Features and targets
- Regression vs classification
- Train/test split
- Cross-validation
- Scaling
- Encoding categorical variables
- Loss functions
- MAE
- MSE
- RMSE
- R²
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix
- Overfitting
- Underfitting
- Regularization
- Residual analysis

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 001 | Linear Regression: Housing Prices | Tabular regression | Baseline, Linear Regression |
| 002 | Regularized Regression: Housing Prices | Tabular regression | Ridge, Lasso, ElasticNet |
| 003 | Logistic Regression: Medical Diagnosis | Tabular classification | Baseline, Logistic Regression |
| 004 | Polynomial Regression: Nonlinear Synthetic Data | Synthetic regression | Linear, Polynomial Regression |
| 005 | Classification Metrics Deep Dive | Tabular classification | Logistic Regression |

## Completion Criteria

- Regression and classification workflows are both implemented.
- At least one task includes residual plots.
- At least one task includes confusion matrix analysis.
- Every model is compared against a dumb baseline.
- Regularization is explained with real results.

---

# Phase 2 — Nonlinear Classical ML

## Goal

Move from linear decision boundaries to nonlinear models and stronger tabular ML methods.

This phase should build intuition for when simple models fail and how trees, kernels, and ensembles improve performance.

## Models

- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Extra Trees
- Support Vector Machine
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

## Concepts

- Nonlinear decision boundaries
- Tree splits
- Entropy and Gini impurity
- Bagging
- Boosting
- Feature importance
- Hyperparameter tuning
- Grid search
- Random search
- Cross-validation
- Class imbalance
- Precision-recall tradeoff
- Probability calibration

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 006 | Decision Trees: Credit Risk | Tabular classification | Decision Tree |
| 007 | Random Forest: Bank Marketing | Tabular classification | Random Forest |
| 008 | SVM: Nonlinear Classification | Tabular/synthetic | SVM |
| 009 | Gradient Boosting Benchmark | Tabular classification | Gradient Boosting, XGBoost/LightGBM |
| 010 | Class Imbalance Experiment | Tabular classification | Logistic Regression, Random Forest, Boosting |

## Completion Criteria

- At least three nonlinear models are compared.
- A hyperparameter tuning experiment is completed.
- Feature importance is visualized.
- One imbalanced classification task is analyzed properly.
- Failure cases are documented.

---

# Phase 3 — Unsupervised Learning

## Goal

Learn how to extract structure from unlabeled data.

This phase should focus less on leaderboard-style accuracy and more on interpretation, visualization, and understanding.

## Models

- K-Means
- DBSCAN
- Gaussian Mixture Models
- PCA
- t-SNE
- UMAP
- Isolation Forest
- Local Outlier Factor

## Concepts

- Clustering
- Distance metrics
- Dimensionality reduction
- Latent structure
- Silhouette score
- Elbow method
- Cluster interpretation
- Outlier detection
- Density-based methods
- Visualization pitfalls

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 011 | Customer Segmentation | Tabular | K-Means, GMM |
| 012 | PCA Visualization | Tabular/image features | PCA |
| 013 | t-SNE vs UMAP Comparison | High-dimensional data | t-SNE, UMAP |
| 014 | Anomaly Detection | Tabular | Isolation Forest, LOF |
| 015 | DBSCAN Clustering | Spatial/synthetic | DBSCAN |

## Completion Criteria

- At least two clustering algorithms are compared.
- At least two dimensionality reduction methods are compared.
- One anomaly detection task is completed.
- Cluster interpretation is written clearly.
- The limitations of unsupervised metrics are documented.

---

# Phase 4 — Time-Series and Sequential Data

## Goal

Understand temporal data, forecasting, and sequence-aware validation.

The key focus is avoiding leakage and learning how time-series problems differ from normal random-split ML.

## Models

- Naive forecast
- Moving average
- Exponential smoothing
- Linear Regression with lag features
- Random Forest with lag features
- Gradient Boosting with lag features
- ARIMA-style baseline
- LSTM/GRU later as deep learning extension

## Concepts

- Time-based splits
- Lag features
- Rolling windows
- Forecast horizons
- Trend
- Seasonality
- Autocorrelation
- Data leakage in time-series
- Walk-forward validation
- MAE/RMSE/MAPE for forecasting

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 016 | Basic Forecasting: Energy Demand | Time-series | Naive, Moving Average |
| 017 | Lag Feature Forecasting | Time-series | Linear Regression, Random Forest |
| 018 | Multi-step Forecasting | Time-series | Classical ML |
| 019 | Time-Series Leakage Case Study | Time-series | Any |
| 020 | Sequence Classification Baseline | Sequential/tabular | Classical ML |

## Completion Criteria

- No random split is used for forecasting tasks.
- At least one walk-forward validation is implemented.
- A naive forecast baseline is included.
- Forecast plots are generated.
- Leakage risks are explained.

---

# Phase 5 — Probabilistic Models and HMMs

## Goal

Rebuild probabilistic ML intuition and understand sequence models before modern deep learning.

This phase is important because it develops reasoning around uncertainty, hidden states, and generative assumptions.

## Models

- Naive Bayes
- Gaussian Naive Bayes
- Multinomial Naive Bayes
- Bayesian Regression
- Gaussian Mixture Models
- Markov Chains
- Hidden Markov Models

## Concepts

- Bayes theorem
- Conditional probability
- Prior and posterior
- Likelihood
- Independence assumptions
- Generative vs discriminative models
- Markov assumption
- Hidden states
- Emission probabilities
- Transition probabilities
- Viterbi algorithm
- Forward algorithm

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 021 | Naive Bayes: Text Classification | Text | Multinomial Naive Bayes |
| 022 | Gaussian Naive Bayes: Medical Data | Tabular | Gaussian NB |
| 023 | Markov Chain: Weather Simulation | Sequential | Markov Chain |
| 024 | HMM: Part-of-Speech Tagging | Text sequence | Hidden Markov Model |
| 025 | HMM: Regime Detection | Time-series | Gaussian HMM |

## Completion Criteria

- Naive Bayes is implemented and compared with Logistic Regression.
- A Markov Chain is built from scratch.
- At least one HMM task is completed.
- Viterbi decoding is explained.
- Model assumptions are documented clearly.

---

# Phase 6 — Deep Learning Basics

## Goal

Move from classical ML to neural networks while keeping the same experiment discipline.

This phase should focus on understanding tensors, optimization, loss curves, and failure modes before jumping into large models.

## Models

- MLP
- Autoencoder
- CNN intro
- RNN intro
- LSTM intro
- GRU intro

## Concepts

- Tensors
- Forward pass
- Backpropagation
- Optimizers
- Learning rate
- Epochs and batches
- Loss curves
- Activation functions
- Dropout
- Batch normalization
- Weight initialization
- Overfitting in neural networks
- GPU usage
- Checkpointing

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 026 | MLP: Fashion-MNIST | Image/tabularized | MLP |
| 027 | MLP: Tabular Classification | Tabular | MLP |
| 028 | Autoencoder: Anomaly Detection | Tabular/image | Autoencoder |
| 029 | RNN/LSTM: Sequence Classification | Text/sequence | RNN, LSTM |
| 030 | Training Loop From Scratch | Synthetic/simple | PyTorch MLP |

## Completion Criteria

- A neural network training loop is written and understood.
- Loss curves are plotted.
- At least one overfitting experiment is shown.
- At least one checkpoint is saved and loaded.
- A neural model is compared against a classical baseline.

---

# Phase 7 — Computer Vision

## Goal

Practice image-based ML from simple CNNs to transfer learning and segmentation.

## Models

- CNN from scratch
- ResNet transfer learning
- MobileNet/EfficientNet transfer learning
- U-Net
- Object detection baseline
- CLIP-style embeddings for similarity search

## Concepts

- Image tensors
- Channels
- Convolutions
- Pooling
- Data augmentation
- Transfer learning
- Fine-tuning
- Object detection
- Semantic segmentation
- IoU
- Dice score
- Grad-CAM/error visualization

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 031 | CNN: Fashion-MNIST/CIFAR-10 | Image classification | CNN |
| 032 | Transfer Learning: Small Image Dataset | Image classification | ResNet/MobileNet |
| 033 | Image Augmentation Study | Image classification | CNN/Transfer Learning |
| 034 | Segmentation: Road/Medical/Waste Masks | Image segmentation | U-Net |
| 035 | Image Similarity Search | Images | Embeddings + Nearest Neighbors |

## Completion Criteria

- CNN from scratch is implemented.
- Transfer learning is completed.
- Augmentation impact is measured.
- One segmentation task is completed.
- Computer vision errors are visualized.

---

# Phase 8 — Natural Language Processing

## Goal

Practice text ML from classical bag-of-words models to transformer fine-tuning.

This phase should connect strongly to previous financial sentiment and hallucination-evaluation work.

## Models

- Bag-of-Words
- TF-IDF
- Naive Bayes
- Logistic Regression
- SVM
- Word2Vec-style embeddings
- LSTM
- Transformer fine-tuning
- Sentence embeddings
- Retrieval baseline

## Concepts

- Tokenization
- Stop words
- N-grams
- TF-IDF
- Embeddings
- Sequence models
- Attention
- Transformers
- Fine-tuning
- Text classification metrics
- Retrieval evaluation
- Hallucination/error analysis

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 036 | Sentiment Analysis: TF-IDF Baseline | Text | TF-IDF + Logistic Regression |
| 037 | Naive Bayes vs Logistic Regression | Text | NB, Logistic Regression |
| 038 | Word Embedding Classifier | Text | Embeddings + Classifier |
| 039 | LSTM Text Classification | Text sequence | LSTM |
| 040 | Transformer Fine-Tuning | Text | DistilBERT/BERT |
| 041 | Retrieval QA Baseline | Text documents | Embeddings + Vector Search |

## Completion Criteria

- Classical NLP baseline is implemented.
- A sequence model is trained.
- A transformer is fine-tuned or used for embeddings.
- Text errors are categorized.
- At least one retrieval-style task is completed.

---

# Phase 9 — Audio and Speech

## Goal

Understand audio as data and practice both classical and deep learning approaches.

## Models

- MFCC + Logistic Regression
- MFCC + Random Forest
- Spectrogram CNN
- LSTM/GRU for audio sequences
- Transfer learning with audio embeddings

## Concepts

- Waveforms
- Sampling rate
- STFT
- Spectrograms
- Mel spectrograms
- MFCCs
- Audio augmentation
- Audio classification
- Speaker/task variation
- Noise robustness

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 042 | Audio Features: MFCC Classification | Audio | MFCC + Random Forest |
| 043 | Speech Commands Classification | Audio | Spectrogram CNN |
| 044 | Audio Augmentation Study | Audio | Classical + CNN |
| 045 | Speaker/Emotion Classification | Audio | Classical + Deep |
| 046 | Audio Sequence Model | Audio sequence | LSTM/GRU |

## Completion Criteria

- MFCC features are extracted and explained.
- Spectrograms are visualized.
- Classical audio model is compared with CNN.
- Audio augmentation is tested.
- Audio error cases are documented.

---

# Phase 10 — Recommenders and Ranking

## Goal

Practice recommendation systems, similarity search, and ranking metrics.

## Models

- Popularity baseline
- User-user collaborative filtering
- Item-item collaborative filtering
- Matrix factorization
- Content-based recommendation
- Embedding similarity
- Learning-to-rank baseline

## Concepts

- User-item matrix
- Sparsity
- Cold start
- Similarity metrics
- Collaborative filtering
- Matrix factorization
- Implicit vs explicit feedback
- Precision@K
- Recall@K
- MAP
- NDCG

## Recommended Tasks

| ID | Task | Dataset Type | Models |
|---|---|---|---|
| 047 | Movie Recommendation Baseline | User-item | Popularity, Similarity |
| 048 | Collaborative Filtering | User-item | User-user, Item-item |
| 049 | Matrix Factorization | User-item | SVD/ALS |
| 050 | Content-Based Recommendation | Text/tabular | TF-IDF/Embeddings |
| 051 | Ranking Metrics Study | Ranking | Recommender models |

## Completion Criteria

- Popularity baseline is implemented.
- Collaborative filtering is implemented.
- Matrix factorization is implemented.
- Ranking metrics are calculated.
- Cold-start limitations are documented.

---

# Phase 11 — Capstone Projects

## Goal

Build portfolio-quality ML systems that combine multiple phases.

Each capstone should feel like a complete applied ML project with data ingestion, training, evaluation, reporting, and deployment/demo potential.

## Capstone Ideas

| ID | Capstone | Areas Covered |
|---|---|---|
| 052 | End-to-End Tabular ML Pipeline | Tabular, preprocessing, modeling, evaluation |
| 053 | DDoS Detection Revisited | Tabular/time-series, SentinelAI-style detection |
| 054 | Waste Classification Revisited | Computer vision, WasteWise-style classifier |
| 055 | Financial Sentiment Benchmark | NLP, classical ML, transformers |
| 056 | Audio Classifier System | Audio, classical ML, deep learning |
| 057 | RAG Hallucination Evaluator | NLP, retrieval, evaluation, Analytics Depot-style testing |
| 058 | Mini AutoML Benchmark | Multiple datasets, multiple models |
| 059 | Multimodal ML Experiment | Text + image/audio/tabular |
| 060 | Final ML Portfolio Report | Documentation, model comparison, lessons learned |

## Completion Criteria

- Each capstone has a complete report.
- Each capstone includes baseline and advanced model comparison.
- Each capstone has reproducible code.
- Each capstone has clear limitations.
- At least three capstones are polished enough for portfolio use.

---

# Task Lifecycle

Every task should move through these stages:

```txt
TODO -> IN_PROGRESS -> EXPERIMENTING -> REPORTING -> DONE
```

## TODO

Task is planned but not started.

## IN_PROGRESS

Dataset and goal are selected. Initial notebook or script exists.

## EXPERIMENTING

Models are being trained, evaluated, and compared.

## REPORTING

Results are done. Report and README are being finalized.

## DONE

Task has:

- README
- Dataset notes
- Baseline model
- Main model
- Metrics
- Plots or tables
- Error analysis
- Final report
- What I learned
- Next steps

---

# Standard Task Folder Structure

Each task should follow this structure:

```txt
tasks/001_task_name/
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

For early learning tasks, a notebook-only workflow is acceptable.

After Phase 1, each serious task should include scripts where possible.

---

# Standard Experiment Rules

1. Every task must include a dumb baseline.
2. Every dataset must have source, target, feature, and license notes.
3. Every model must be evaluated using metrics appropriate for the task.
4. Never use random train/test splits for time-series forecasting.
5. Never report accuracy alone for imbalanced classification.
6. Never tune on the test set.
7. Always document failure cases.
8. Always write what was learned.
9. Keep raw datasets out of Git unless they are tiny and license-safe.
10. Prefer reproducible scripts over notebook-only experiments as the repo matures.

---

# Current Starting Sprint

The first sprint should focus on getting comfortable with the full supervised ML loop.

## Sprint 1: Foundations

| Task ID | Task | Primary Goal | Status |
|---|---|---|---|
| 001 | Linear Regression: California Housing | Learn full regression workflow | TODO |
| 002 | Ridge/Lasso: California Housing | Understand regularization | TODO |
| 003 | Logistic Regression: Breast Cancer | Learn binary classification workflow | TODO |
| 004 | Decision Tree: Bank Marketing or Adult Income | First nonlinear classifier | TODO |
| 005 | Metrics Deep Dive | Understand classification/regression metrics | TODO |

## Sprint 1 Completion Criteria

Sprint 1 is complete when:

- At least three tasks are DONE.
- Regression and classification are both covered.
- Linear and nonlinear models are both covered.
- Baselines are used in every task.
- Reports are written clearly enough for future revision.

---

# Suggested Dataset Sources

Use simple, well-known, low-friction datasets first.

## Early Phase Sources

- scikit-learn built-in and fetched datasets
- UCI Machine Learning Repository
- OpenML
- Kaggle, only when the dataset is easy to download and licensing is clear

## Later Phase Sources

- Hugging Face Datasets
- TorchVision datasets
- Librosa-compatible audio datasets
- Domain-specific public datasets
- Previously used personal project datasets, when allowed

---

# Model Coverage Checklist

## Supervised Classical ML

- [ ] Linear Regression
- [ ] Ridge Regression
- [ ] Lasso Regression
- [ ] ElasticNet
- [ ] Logistic Regression
- [ ] KNN
- [ ] Naive Bayes
- [ ] Decision Tree
- [ ] Random Forest
- [ ] SVM
- [ ] Gradient Boosting
- [ ] XGBoost
- [ ] LightGBM
- [ ] CatBoost

## Unsupervised ML

- [ ] K-Means
- [ ] DBSCAN
- [ ] Gaussian Mixture Models
- [ ] PCA
- [ ] t-SNE
- [ ] UMAP
- [ ] Isolation Forest
- [ ] Local Outlier Factor

## Probabilistic and Sequential Models

- [ ] Bayesian Regression
- [ ] Markov Chain
- [ ] Hidden Markov Model
- [ ] Gaussian HMM
- [ ] Sequence labeling model

## Deep Learning

- [ ] MLP
- [ ] CNN
- [ ] RNN
- [ ] GRU
- [ ] LSTM
- [ ] Autoencoder
- [ ] Transformer
- [ ] U-Net

## Applied Systems

- [ ] Recommender system
- [ ] Ranking model
- [ ] Retrieval system
- [ ] Image classifier
- [ ] Audio classifier
- [ ] Text classifier
- [ ] Time-series forecaster
- [ ] End-to-end ML pipeline

---

# Data Type Coverage Checklist

- [ ] Small tabular
- [ ] Medium tabular
- [ ] Imbalanced tabular
- [ ] Text
- [ ] Images
- [ ] Audio
- [ ] Time-series
- [ ] Sequential labels
- [ ] User-item recommendation data
- [ ] Multimodal data
- [ ] Synthetic data
- [ ] Real-world noisy data

---

# Progress Tracking Format

Use this format inside `PROGRESS.md`:

```md
# Progress Log

## YYYY-MM-DD

### Completed
- 

### Learned
- 

### Problems
- 

### Next
- 
```

Use this format inside `EXPERIMENT_LOG.md`:

```md
# Experiment Log

| Date | Task | Dataset | Model | Metric | Result | Notes |
|---|---|---|---|---|---|---|
| YYYY-MM-DD | 001 | California Housing | Linear Regression | RMSE/R² | TBD | First baseline |
```

---

# Priority Rule

Do not jump randomly between cool topics.

Follow this priority order:

1. Finish the current task.
2. Write the report.
3. Update the task tracker.
4. Only then start the next task.

The repo should reward completion, not chaos.

---

# Immediate Next Step

Start with:

```txt
tasks/001_linear_regression_california_housing/
```

Task 001 should cover:

- loading the California Housing dataset
- basic EDA
- train/test split
- mean baseline
- Linear Regression
- MAE, RMSE, R²
- residual analysis
- final report
- what linear regression assumes
- what the model gets wrong

After Task 001 is complete, move to Task 002 using the same dataset with Ridge, Lasso, and ElasticNet.

---

# Long-Term Definition of Done

Unlearning ML is successful when the repo contains:

- 50+ completed ML tasks
- 10+ model families
- 8+ data types
- 5+ polished reports
- 3+ capstone projects
- reusable ML utilities
- clear experiment logs
- strong enough documentation to revise ML quickly months later
