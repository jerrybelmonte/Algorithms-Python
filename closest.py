# Uses python3
import sys
import math


def minimum_distance(x, y):
    # write your code here
    return 10 ** 18


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    data = [2, 0, 0, 3, 4]
    # data = [4, 7, 7, 1, 100, 4, 8, 7, 7]
    # data = [11, 4, 4, -2, -2, -3, -4, -1, 3, 2, 3, -4, 0, 1, 1, -1, -1, 3, -1, -4, 2, -2, 4]
    n = data[0]
    x_ = data[1::2]
    y_ = data[2::2]
    print("{0:.9f}".format(minimum_distance(x_, y_)))
