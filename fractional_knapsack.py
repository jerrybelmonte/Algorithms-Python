# Maximum Value of the Loot (Fractional Knapsack)
# Author: jerrybelmonte
# Input: First line containst he number n of the items and the capacity W.
# The following lines contain the values and weights of each i-th item.
# Output: The maximal value of fractions of the items.
import sys
from collections import namedtuple

Knapsack = namedtuple('Knapsack', 'weight fraction')


def get_optimal_value(capacity: int, weights: list, values: list):
    """
    Greedy algorithm for the optimal knapsack value.

    :param capacity: the weight capacity of the knapsack
    :param weights: the list of weights for each item
    :param values: the list of calues for each item
    :return: the optimal fractional knapsack value

    Example 1: We take the first item and the third item.
    >>> get_optimal_value(50, [20, 50, 30], [60, 100, 120])
    180.0

    Example 2: We take only a third of the only item.
    >>> get_optimal_value(10, [30], [500])
    166.66666666666669
    """
    max_value = 0.0
    loot = sorted([Knapsack(weights[i], values[i]/weights[i])
                   for i in range(len(weights))],
                  key=lambda knapsack: knapsack.fraction,
                  reverse=True)

    for i in range(len(loot)):
        if capacity == 0:
            return max_value

        value = min(loot[i].weight, capacity)
        max_value += value * loot[i].fraction
        capacity -= value

    return max_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2: (2 * n + 2): 2]
    weights = data[3: (2 * n + 2): 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
