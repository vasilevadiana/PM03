#!/usr/bin/env python3

import sys


def parse_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}

    for element in sys.argv[1:]:
        try:
            key, value = element.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{element}'")
            continue

        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue

        try:
            inventory[key] = int(value)
        except ValueError as err:
            print(f"Quantity error for '{key}': {err}")

    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    if sys.argv[1:]:   
        inventory: dict[str, int] = parse_inventory()

        print("Got inventory:", inventory)
        print("Item list:", list(inventory.keys()))

        inventory_sum = sum(inventory.values())
        print(f"Total quantity of the {len(inventory.keys())} "
             f"items: {inventory_sum}")

        for key in inventory:
            print(f"Item {key} represents "
                f"{round(100*inventory[key]/inventory_sum, 1)}%")

        most_abundan = list(inventory)[0]
        least_abundan = list(inventory)[0]
        for key in inventory:
            if inventory[key] > inventory[most_abundan]:
                most_abundan = key
            elif inventory[key] < inventory[least_abundan]:
                least_abundan = key
        print(f"Item most abundan: {most_abundan} "
            f"with quantity {inventory[most_abundan]}")
        print(f"Item least abundan: {least_abundan} "
            f"with quantity {inventory[least_abundan]}")

        inventory["diana"] = 1
        print("Updated inventory:", inventory)
    else:
        print("no argument provided")
