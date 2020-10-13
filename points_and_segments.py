# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    # write your code here
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    data = [2, 3, 0, 5, 7, 10, 1, 6, 11]
    # data = [1, 3, -10, 10, -100, 100, 0]
    # data = [3, 2, 0, 5, -3, 2, 7, 10, 1 , 6]
    n = data[0]
    m = data[1]
    start_ = data[2:2 * n + 2:2]
    end_ = data[3:2 * n + 2:2]
    point_ = data[2 * n + 2:]
    # use fast_count_segments
    cnt = naive_count_segments(start_, end_, point_)
    for x in cnt:
        print(x, end=' ')
