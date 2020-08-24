# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    num = len(weights)
    ratios = [values[i]/weights[i] for i in range(num)]
    vals = sorted(ratios)[::-1]
    for i in range(num):
        if capacity == 0:
            return value
        val = vals[i]
        ndx = ratios.index(val)
        a = min(weights[ndx], capacity)
        value += a * val
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
