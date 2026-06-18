#!/usr/bin/env python3

import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")

    i = 0
    scores: list[int] = []
    while i <= len(sys.argv[1:]):
        try:
            scores.append(int(sys.argv[i]))
        except TypeError:
            print("Invalid parameter:", sys.argv[i])
        i += 1
    if len(scores) == 0:
        print("""No scores provided.
        Usage: python3 ft_score_analytics.py <score1> <score2> ...""")
    else:
        print("Scores processed:", scores)
        print("Total players:", len(scores))
        print("Total score:", sum(scores))
        print("Average score:", sum(scores)/len(scores))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))


if __name__ == "__main__":
    score_analytics()
