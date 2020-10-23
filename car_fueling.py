# Car fueling
# Author: jerrybelmonte
# Input: The distance d, the miles per tank m, the number of stops n,
# and the distances of each gas station from the starting point.
# Output: The minimum number of pitstops.
import sys


def compute_min_refills(distance: int, tank: int, stops: list):
    """
    Computes the minimum number of gas station pit stops.

    >>> compute_min_refills(950, 400, [200, 375, 550, 750])
    2

    >>> compute_min_refills(10, 3, [1, 2, 5, 9])
    -1

    Example 3:
    >>> compute_min_refills(200, 250, [100, 150])
    0
    """
    previous, current = 0, 0
    positions = [0] + stops + [distance]

    num_refills, cur_position = 0, 0

    while current <= len(stops):
        previous = current

        while current <= len(stops) and (
                positions[current + 1] - positions[previous]
        ) <= tank:
            current += 1
            cur_position = positions[current]

        if current == previous:
            return -1  # destination not possible

        if cur_position < distance:
            num_refills += 1

    return num_refills


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
