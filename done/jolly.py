# type: ignore
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        els = line.split()
        count = int(els[0])

        nums = [int(n.strip()) for n in els[1:count + 1]]
        pairs = zip(nums[:-1], nums[1:])
        diffs = set(abs(a - b) for a, b in pairs)

        diffs_sum, n = sum(diffs), len(nums) - 1
        comp_sum = n * (n + 1) // 2

        #print(f"{list(diffs)}, {diffs_sum}, {comp_sum}")

        if diffs_sum == comp_sum:
            print("Jolly")
        else:
            print("Not jolly")

main()