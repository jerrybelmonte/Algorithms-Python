# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input_ = sys.stdin.read()
    data = list(map(int, input_.split()))
    n = data[0]
    m = data[n + 1]
    a1 = data[1:n + 1]
    for num in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a1, num), end=' ')
