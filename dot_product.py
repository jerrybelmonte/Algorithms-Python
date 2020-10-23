# Maximum Advertisement Revenue (Maximum Dot Product)
# Author: jerrybelmonte
# Input: First line is an integer n, second line contains sequence a,
# and the third line contains the sequence b.
# Output: The maximum possible value of the two sequences.
import sys


def max_dot_product(a: list, b: list):
    """
    >>> max_dot_product([23], [39])
    897

    >>> max_dot_product([1, 3, -5], [-2, 4, 1])
    23
    """
    a.sort()
    b.sort()

    return sum([a[i]*b[i] for i in range(len(a))])


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
