# type: ignore
import sys
from itertools import zip_longest

def count_carries(i, j):
    i, j = i[::-1], j[::-1]
    carries = 0
    carry = 0
    for k, l in zip_longest(i, j, fillvalue=0):
        if int(k) + int(l) + carry > 9:
            carries += 1
            carry = 1
        else:
            carry = 0
    return carries


def main():
    carries = []
    for line in sys.stdin:
        i, j = line.strip().split(" ")
        if i == '0' and j == '0':
            break
        else:
            carries.append(count_carries(i, j))
    
    for c in carries:
        if c == 0:
            print("No carry operation.")
        elif c == 1:
            print("1 carry operation.")
        else:
            print(f"{c} carry operations.")

main()