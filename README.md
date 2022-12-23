# Benchmark Python 3.10 and 3.11

This repository contains programs that generate random sample data and compute autocorrelation functions. It was made for benchmarking Python 3.10 and 3.11 in typical scientific scenario, when we need to calculate something.

## Results

| OS      | Interpreter version   | Sample 1000      | Sample 10000     | Sample 100000      |
| ------- | --------------------- | ---------------- | ---------------- | ------------------ |
| Mac OS  | Python 3.10.9 (Clang) | 30.2 ms  (1.34x) | 1.807 s  (1.72x) | 179.238 s  (1.72x) |
| Mac OS  | Python 3.11.1 (Clang) | 22.5 ms  (1x)    | 1.050 s  (1x)    | 104.061 s  (1x)    |
| Linux   | Python 3.10.9 (gcc)   | 95.2 ms  (1.47x) | 6.012 s  (1.44x) | 611.790 s  (1.43x) |
| Linux   | Python 3.11.1 (gcc)   | 64.8 ms  (1x)    | 4.158 s  (1x)    | 425.069 s  (1x)    |
| Windows | Python 3.10.9 (msvc)  | 1                | 1                | 1                  |
| Windows | Python 3.11.1 (msvc)  | 1                | 1                | 1                  |

For Linux (Manjaro) and Windows 10 was used laptop: Intel i3-5005U (2 GHz), 8 Gb RAM.

For Mac OS: Macbook Pro M2 (2022).

Table contains minimal result of all (~30) runs.
