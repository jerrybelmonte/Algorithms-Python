# Organizing a Lottery
# Author: jerrybelmonte
import sys
from collections import namedtuple, defaultdict

Point = namedtuple('Point', 'value type')


def count_segments(starts: list, ends: list, line_pts: list):
    """
    Computes the number of segments that contain each point.

    :param starts: list of starting values for the segments
    :param ends: list of end values for the segments
    :param line_pts: list of points on a line
    :return: list of the number of segments that contain a point i

    >>> count_segments([0, 7], [5, 10], [1, 6, 11])
    [1, 0, 0]

    >>> count_segments([-10], [10], [-100, 100, 0])
    [0, 0, 1]

    >>> count_segments([0, -3, 7], [5, 2, 10], [1, 6])
    [2, 0]
    """
    point_count = [0] * len(line_pts)
    points = []
    start_type = -1
    end_type = 1
    point_dict = defaultdict(list)

    # the points will have a value of 0 assigned to them
    for i in range(len(line_pts)):
        points.append(Point(line_pts[i], 0))
        point_dict[line_pts[i]].append(i)

    # the start of a segment will have a value of -1
    points.extend([Point(start_value, start_type)
                   for start_value in starts])

    # the end of a segment will have a value of 1
    points.extend([Point(end_value, end_type)
                   for end_value in ends])

    # sort the list of points by thier value first then by type
    points.sort(key=lambda point: (point.value, point.type))

    coverage = 0
    for pt in points:
        if pt.type == start_type:  # starting point of a segment
            coverage += 1
        elif pt.type == end_type:  # ending point of a segment
            coverage -= 1
        else:  # its a point
            for ndx in point_dict[pt.value]:
                point_count[ndx] = coverage

    return point_count


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    m = data[1]
    start = data[2:2 * n + 2:2]
    end = data[3:2 * n + 2:2]
    pts = data[2 * n + 2:]
    cnt = count_segments(start, end, pts)
    for x in cnt:
        print(x, end=' ')
