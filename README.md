# Benchmark Python 3.10 and 3.11

This repository contains programs that generate random sample data and compute autocorrelation functions. It was made for benchmarking Python 3.10 and 3.11 in typical scientific scenario, when we need to calculate something.

## Results

| OS      | Interpreter version | Sample 1000      | Sample 10000     | Sample 100000      |
| ------- | ------------------- | ---------------- | ---------------- | ------------------ |
| Mac OS  | Python 3.10         | 30.2 ms  (1.34x) | 1.807 s  (1.72x) | 179.238 s  (1.72x) |
| Mac OS  | Python 3.11         | 22.5 ms  (1x)    | 1.050 s  (1x)    | 104.061 s  (1x)    |
| Linux   | Python 3.10         | 1                | 1                | 1                  |
| Linux   | Python 3.11         | 1                | 1                | 1                  |
| Windows | Python 3.10         | 1                | 1                | 1                  |
| Windows | Python 3.11         | 1                | 1                | 1                  |

For Linux (Manjaro) and Windows 10 was used laptop: Intel i3-5005U (2 GHz), 8 Gb RAM.

For Mac OS: Macbook Pro M2 (2022).

Table contains minimal result of all (~30) runs.
