#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: set[str]) -> set[str]:
    random_number: int = random.randint(1, len(achievements))
    random_achievements: set[str] = set(random.sample(list(achievements),
                                                      random_number))
    return random_achievements


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    achievements: set[str] = {'Crafting Genius', 'Strategist', 'World Savior',
                              'Speed Runner', 'Survivor', 'Master Explorer',
                              'Treasure Hunter', 'Unstoppable', 'First Steps',
                              'Collector Supreme', 'Untouchable',
                              'Sharp Mind', 'Boss Slayer'}
    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    print(f"""All distinct achievements: {alice | bob | charlie | dylan}\n""")

    print(f"""Common achievements: {alice & bob & charlie & dylan}\n""")

    print(f"Only Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - bob - alice - dylan}")
    print(f"Only Dylan has: {dylan - charlie - bob - alice}\n")

    print(f"Alice is missing: {achievements - alice}")
    print(f"Bob is missing: {achievements - bob}")
    print(f"Charlie is missing: {achievements - charlie}")
    print(f"Dylan is missing: {achievements - dylan}")
