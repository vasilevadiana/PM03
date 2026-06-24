#!/usr/bin/env python3

import random
from typing import Generator, Tuple, List


def gen_event(players: list[str], actions: list[str]) -> Generator[Tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(event_list: List[Tuple[str, str]]) \
        -> Generator[Tuple[str, str], None, None]:
    while event_list:
        idx = random.randrange(len(event_list))
        yield event_list.pop(idx)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "swim", "climb", "use", "release"]

    gen = gen_event(players, actions)

    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    events = [next(gen) for _ in range(10)]
    print("Built list of 10 events:", events)

    for ev in consume_event(events):
        print("Got event from list:", ev)
        print("Remains in list:", events)
