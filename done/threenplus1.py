# type: ignore

import sys
from functools import cache

@cache
def cycle_len(n):
    if n == 1:
        return 1

    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n //=2

    return 1 + cycle_len(n)

def max_cycle_len(i, j):
    return max(cycle_len(k) for k in range(i, j+1))

def main():
    for line in sys.stdin:
        if not line.strip():
            break
        i, j = line.split()
        i, j = int(i), int(j)
        if j < i:
            i, j  = j, i
            print(f"{j} {i} {max_cycle_len(i, j)}")
        else:
            print(f"{i} {j} {max_cycle_len(i, j)}")

main()
