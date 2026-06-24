#!/usr/bin/env python3

import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    if (len(sys.argv) == 1):
        print("No arguments provided!")
    else:
        print("Arguments received:", len(sys.argv) - 1)
        i: int = 0
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {len(sys.argv)} \n")


if __name__ == "__main__":
    command_quest()
