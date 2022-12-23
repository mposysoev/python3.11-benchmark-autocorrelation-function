#!/bin/sh

hyperfine   "python3.10 autocorrelation-function.py sample_1000.txt" \
            "python3.10 autocorrelation-function.py sample_10000.txt" \
            "python3.11 autocorrelation-function.py sample_1000.txt" \
            "python3.11 autocorrelation-function.py sample_10000.txt" -r 30