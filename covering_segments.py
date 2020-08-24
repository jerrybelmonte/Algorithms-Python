# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    p = [(s.start, s.end) for s in segments]
    p = sorted(p, key=lambda s: s[0])
    cur = p[0]
    end = cur[1]
    point = []
    for i in range(1, len(p)):
        start, stop = p[i][0], p[i][1]
        if end < start:
            point.append(end)
            end = stop
        elif stop < end:
            end = stop
    if end not in point:
        point.append(end)
    return point


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
