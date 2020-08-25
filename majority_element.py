# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    a = sorted(a)
    # print(a)
    cur = left
    ndx = left
    while ndx < right:
        count = 0
        while ndx < right and a[ndx] == a[cur]:
            ndx += 1
            count += 1
        if count > left + ((right - left)//2):
            return ndx
        cur = ndx
    return -1


if __name__ == '__main__':
    input_ = sys.stdin.read()
    n_, *a_ = list(map(int, input_.split()))
    if get_majority_element(a_, 0, n_) != -1:
        print(1)
    else:
        print(0)
