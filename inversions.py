# Number of Inversions
# Author: jerrybelmonte
import sys


def get_number_of_inversions(seq: list, arr: list, left: int, right: int):
    """
    Counts the number of inversions of a given sequence.

    :param seq: sequence of numbers
    :param arr: array filled with zeros
    :param left: starting index
    :param right: ending index
    :return: number of inversions

    Example: there are two inversions: (a1, a3) 3 > 2, and (a2, a3) 9 > 2
    >>> get_number_of_inversions([2, 3, 9, 2, 9], [0, 0, 0, 0, 0], 0, 5)
    2
    """
    num_inversions = 0

    if right - left <= 1:
        return num_inversions

    mid = (left + right)//2
    num_inversions += get_number_of_inversions(seq, arr, left, mid)
    num_inversions += get_number_of_inversions(seq, arr, mid, right)
    num_inversions += merge(seq, arr, left, mid, right)

    return num_inversions


def merge(seq, arr, left, mid, right):
    i, k, j = left, left, mid
    inversion_count = 0

    while i < mid and j < right:
        if seq[i] <= seq[j]:  # non-decreasing
            arr[k] = seq[i]
            k += 1
            i += 1
        else:  # inversion detected
            arr[k] = seq[j]
            j += 1
            k += 1
            inversion_count += mid - i

    while i < mid:
        arr[k] = seq[i]
        i += 1
        k += 1

    while j < right:
        arr[k] = seq[j]
        j += 1
        k += 1

    for ndx in range(left, right):
        seq[ndx] = arr[ndx]

    return inversion_count


if __name__ == '__main__':
    n, *a = list(map(int, sys.stdin.read().split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, n))
