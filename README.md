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
export HF_DATASETS_CACHE="/path/to/cache/directory"
python run_test.py
```

## Results

| Config      | Speed |
| ----------- | ----------- |
| lambda_cloud-8xA100-Israel-home  | 4.0 Gb/s |
| lambda_cloud-8xV100-Texas-persistent   |  2.0 Gb/s (4.6 Gb/s afterwards unless reboot) |
| lambda_cloud-8xV100-Texas-home   |  4.7 Gb/s |
| sshfs-lambda_cloud-8xV100-Texas-persistent   | 0.03Gb/s |
