from random import random

N = 100_000

precision = 5
width = 8

with open(f"sample_{N}.txt", "w") as file:

    for _ in range(N):
        x = 2 * random() - 1
        y = 2 * random() - 1
        z = 2 * random() - 1

        print(
            f"{x:{width}.{precision}f}\t\t{y:{width}.{precision}f}\t\t{z:{width}.{precision}f}",
            file=file,
        )
