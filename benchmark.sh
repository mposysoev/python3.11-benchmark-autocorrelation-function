#!/bin/sh

hyperfine   "python3.10 auto-cor-fun.py sample_1000.txt" \
            "python3.10 auto-cor-fun.py sample_10000.txt" \
            "python3.10 auto-cor-fun.py sample_100000.txt" \
            "python3.11 auto-cor-fun.py sample_1000.txt" \
            "python3.11 auto-cor-fun.py sample_10000.txt" \
            "python3.11 auto-cor-fun.py sample_100000.txt" -r 3