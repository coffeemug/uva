# type: ignore
import sys

def median(seq):
    if len(seq) == 1:
        return seq[0]
    elif len(seq) % 2 == 1:
        return seq[len(seq) // 2]
    else:
        return (seq[len(seq) // 2 - 1] + seq[len(seq) // 2]) // 2

def main():
    ncases = int(sys.stdin.readline().strip())
    for _ in range(ncases):
        rels = sorted([int(rel.strip()) for rel in  sys.stdin.readline().split()[1:]])
        opt = median(rels)
        print(sum(abs(h - opt) for h in rels))

main()