#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    try:
        x, y, z = input("Enter new coordinates"
                        "as floats in format 'x,y,z': ").split(',')
        coordinates = (float(x), float(y), float(z))
    except ValueError:
        print("Invalid syntax")
        return get_player_pos()
    return coordinates


def coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    dot1 = get_player_pos()
    print("Got a first tuple:", dot1)
    print(f"It includes: X={dot1[0]}, Y={dot1[1]}, Z={dot1[2]}")
    distance1 = math.sqrt((dot1[0])**2 + (dot1[1])**2 + (dot1[2])**2)
    print(f"Distance to center: {round(distance1, 4)}\n")

    print("Get a second set of coordinates")
    dot2 = get_player_pos()
    distance2 = math.sqrt((dot2[0] - dot1[0])**2 +
                          (dot2[1] - dot1[1])**2 +
                          (dot2[2] - dot1[2])**2)
    print("Distance between the 2 sets of coordinates:", round(distance2, 4))


if __name__ == "__main__":
    coordinate_system()
