# Randomized Quicksort with 3-way Partition
# Author: jerrybelmonte
import sys
from random import randint


def partition3(seq, lo, hi):
    left, right = lo, hi
    ndx = lo + 1
    pivot = seq[lo]

    while ndx <= right:
        if seq[ndx] < pivot:
            seq[left], seq[ndx] = seq[ndx], seq[left]
            left, ndx = left + 1, ndx + 1
        elif seq[ndx] > pivot:
            seq[ndx], seq[right] = seq[right], seq[ndx]
            right -= 1
        else:
            ndx += 1

    return left, right


def randomized_quick_sort(seq, left, right):
    if left >= right:  # base case
        return

    rand_ndx = randint(left, right)  # random selection
    seq[left], seq[rand_ndx] = seq[rand_ndx], seq[left]

    mid_left, mid_right = partition3(seq, left, right)
    randomized_quick_sort(seq, left, mid_left - 1)
    randomized_quick_sort(seq, mid_right + 1, right)


def quick_sort(seq: list):
    """
    Randomized quicksort with 3-way partition implementation.

    :param seq: sequence of numbers
    :return: sorted sequence in non-decreasing order

    >>> quick_sort([2, 3, 9, 2, 2])
    [2, 2, 2, 3, 9]
    """
    randomized_quick_sort(seq, 0, len(seq) - 1)
    return seq


if __name__ == '__main__':
    n, *a = list(map(int, sys.stdin.read().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
