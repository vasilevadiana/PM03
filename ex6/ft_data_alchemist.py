#!/usr/bin/env python3

import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    players = ['Alice', 'bob', 'Charlie', 'dylan',
               'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    players_capitalized = [x.capitalize() for x in players]
    print(f"New list with all names capitalized: {players_capitalized}")

    capitalized_only = [x for x in players if x and x[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}\n")

    scores = {name: random.randint(0, 1000) for name in players_capitalized}
    print(f"Score dict: {scores}")

    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    high_scores = {key: value for key, value in scores.items() if value > avg}
    print(f"High scores: {high_scores}")
