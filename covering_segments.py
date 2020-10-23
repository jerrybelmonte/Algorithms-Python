# Collecting Signatures (Covering Segments by Points)
# Author: jerrybelmonte
# Input: First line contains the number of segments n.
# The following lines contains two integers ai and bi for the segment i.
# Output: The minimum number m of points in the first line.
# Followed by the integer coordinates of m points separated by a space.
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    """
    Example 1:
    >>> optimal_points([(1, 3), (2, 5), (3, 6)])
    [3]

    Example 2:
    >>> optimal_points([(4, 7), (1, 3), (2, 5), (5, 6)])
    [3, 6]
    """
    segments.sort(key=lambda s: s[0])
    end = segments[0][1]
    point = []

    for i in range(1, len(segments)):
        start, stop = segments[i]

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
    segments = list(map(lambda x: Segment(
        x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
