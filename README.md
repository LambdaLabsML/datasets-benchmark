# Dataset Benchmark

This repo benchmarks storage using Huggingfaces' datasets.

## Install

```
virtualenv -p /usr/bin/python3.8 venv && \
. venv/bin/activate && \
pip install -r requirements.txt
```

## Run test

```
export HF_DATASETS_CACHE="/path/to/another/directory"
python run_test.py
```

