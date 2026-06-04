#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name unlearning-ml --display-name "Python (unlearning-ml)"

echo "Environment ready. Activate with: source .venv/bin/activate"
