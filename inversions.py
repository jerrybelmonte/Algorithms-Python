# Uses python3
import sys


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # write your code here
    number_of_inversions += merge(a, b, left, ave, right)
    return number_of_inversions


def merge(a, b, lo, mid, hi):
    # Merge a[lo..mid] with a[mid+1..hi]
    i, j = lo, mid + 1
    inversion_count = 0
    # Merge back to a[lo..hi]
    for k in range(lo, hi):
        if a[i] > a[mid]:
            b[j] = a[k]
            j += 1
            inversion_count += 1
        elif j > hi:
            b[i] = a[k]
            i += 1
            inversion_count += 1
        elif a[j] < a[i]:
            b[j] = a[k]
            j += 1
            inversion_count += 1
        else:
            b[i] = a[k]
            i += 1
    return inversion_count


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n_, *a_ = list(map(int, input.split()))
    n_ = 5
    a_ = [2, 3, 9, 2, 9]
    b_ = n_ * [0]
    print(get_number_of_inversions(a_, b_, 0, len(a_)))
