# Majority Element
# Author: jerrybelmonte
import sys


def get_majority_element(seq, left, right):
    """
    Gets the element in the sequence that makes up the majority if it exists.

    :param seq: sequence of elements
    :param left: starting index in the sequence
    :param right: end index in the sequence
    :return: the majority element count, otherwise -1 if DNE

    >>> get_majority_element([2, 3, 9, 2, 2], 0, 5)
    3

    >>> get_majority_element([1, 2, 3, 4], 0, 4)
    -1

    >>> get_majority_element([1, 2, 3, 1], 0, 4)
    -1
    """
    if left == right:
        return -1

    if left + 1 == right:
        return seq[left]

    seq.sort()
    cur = left
    ndx = left

    while ndx < right:
        count = 0

        while ndx < right and seq[ndx] == seq[cur]:
            ndx += 1
            count += 1

        if count > left + ((right - left)//2):
            return ndx

        cur = ndx

    return -1


if __name__ == '__main__':
    n, *a = list(map(int, sys.stdin.read().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
