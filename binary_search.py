# Binary Search
# Author: jerrybelmonte
import sys


def binary_search(num_seq: list, key_val: int):
    """
    Binary search algorithm implementation.

    :param num_seq: sorted sequence of n pairwise distinct positive integers
    :param key_val: key value to search for in the sequence of numbers
    :return: the index of the element within the sequence of numbers

    >>> binary_search([1, 5, 8, 12, 13], 8)
    2

    >>> binary_search([1, 5, 8, 12, 13], 23)
    -1

    >>> binary_search([1, 5, 8, 12, 13], 1)
    0

    >>> binary_search([1, 5, 8, 12, 13], 11)
    -1
    """
    left, right = 0, len(num_seq) - 1

    while left <= right:
        mid = left + (right - left)//2

        if num_seq[mid] == key_val:
            return mid
        elif key_val < num_seq[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    m = data[n + 1]
    a = data[1:n + 1]
    for num in data[n + 2:]:
        print(binary_search(a, num), end=' ')
