# Uses python3
import sys
import random


def partition3(a, lo, hi):
    left, right = lo, hi
    i = lo + 1
    x_val = a[lo]
    while i <= right:
        if a[i] < x_val:
            a[left], a[i] = a[i], a[left]
            left, i = left + 1, i + 1
        elif a[i] > x_val:
            a[i], a[right] = a[right], a[i]
            right -= 1
        else:
            i += 1
    return left, right


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input_ = sys.stdin.read()
    n, *a_ = list(map(int, input_.split()))
    randomized_quick_sort(a_, 0, n - 1)
    for x in a_:
        print(x, end=' ')
