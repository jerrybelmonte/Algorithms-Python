# python3
import sys


def compute_min_refills(distance, tank, stops):
    n = len(stops)
    prev, cur = 0, 0
    d = [0] + stops + [distance]
    num_refills, cur_position = 0, 0
    while cur <= n:
        prev = cur
        while cur <= n and (d[cur+1] - d[prev]) <= tank:
            cur += 1
            cur_position = d[cur]
        if cur == prev:
            return -1
        if cur_position < distance:
            num_refills += 1
    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
