#!/usr/bin/python

import sys
from itertools import permutations


def rock_paper_scissors(n):
    possible_moves = ["rock", "paper", "scissors"]
    possible_rounds = [list(x) for x in permutations(possible_moves,n)]
    return possible_rounds



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
