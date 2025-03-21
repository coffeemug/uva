# type: ignore

import sys
from dataclasses import dataclass
from typing import List
from collections import Counter

@dataclass
class Election:
    candidates: List[str]
    ballots: List[List[int]]

def parse_input():
    ncases = int(sys.stdin.readline())
    sys.stdin.readline()

    for _ in range(ncases):
        ncandidates = int(sys.stdin.readline())
        names = []

        for _ in range(ncandidates):
            names.append(sys.stdin.readline())

        ballots = []
        for ballot in sys.stdin:
            if not ballot.strip():
                break
            ballots.append([int(vote) for vote in ballot.split()])

        yield Election(names, ballots)

def eval_election(ballots: List[List[int]]) -> [int]:
    votes = [ballot[0] for ballot in ballots]
    counts = Counter(votes)
    top_candidate_idx, top_vote_count = counts.most_common(1)[0]
    if top_vote_count > counts.total() // 2:
        return [top_candidate_idx]
    
    # No clear winner. Eliminate candidates tied for lowest vote

    
    raise Exception("not implemented")


def main():
    for election in parse_input():
        winners = eval_election(election.ballots)
        for winner in winners:
            print(election.candidates[winner])
        print()

main()