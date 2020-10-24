# Closest Pair of Points
# Author: jerrybelmonte
import sys
from math import sqrt, ceil
from collections import namedtuple

Point = namedtuple('Point', 'x y')


def euclidian_distance(x1: int, y1: int, x2: int, y2: int):
    return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def naive_min_distance(pts: list):
    num_pts = len(pts)

    if num_pts <= 2:  # base case
        return euclidian_distance(*pts[0], *pts[1])

    min_distance = float(sys.maxsize)

    for i in range(num_pts):
        for j in range(i + 1, num_pts):
            distance = euclidian_distance(*pts[i], *pts[j])
            if distance <= min_distance:
                min_distance = distance

    return min_distance


def minimum_distance(x_coord: list, y_coord: list):
    """
    Computes the minimum distance between the points.

    :param x_coord: list of x coordinates of the points
    :param y_coord: list of y coordinates of the points
    :return: the minimum distance

    >>> minimum_distance([0, 3], [0, 4])
    5.0

    >>> minimum_distance([7, 1, 7], [7, 100, 7])
    0.0

    >>> minimum_distance([7, 1, 4, 7], [7, 100, 8, 7])
    0.0

    >>> minimum_distance([0, 5, 3, 7], [0, 6, 4, 2])
    2.8284271247461903

    >>> minimum_distance([4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2], [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4])
    1.4142135623730951
    """
    num_pts = len(x_coord)

    if num_pts <= 2:  # base case
        return euclidian_distance(x_coord[0], y_coord[0],
                                  x_coord[1], y_coord[1])

    points = [Point(x_coord[i], y_coord[i]) for i in range(num_pts)]
    x_points = sorted(points, key=lambda point: (point.x, point.y))
    y_points = sorted(points, key=lambda point: (point.y, point.x))

    return recursive_min_distance(x_points, y_points)


def recursive_min_distance(x_pts, y_pts):
    num_pts = len(x_pts)

    if num_pts <= 3:
        return naive_min_distance(x_pts)

    mid = ceil(num_pts/2)
    x_left, x_right = x_pts[:mid], x_pts[mid:]
    y_left, y_right = [], []
    xl_set = set(x_left)

    for pt in y_pts:
        if pt in xl_set:
            y_left.append(pt)
        else:
            y_right.append(pt)

    delta_left = recursive_min_distance(x_left, y_left)
    delta_right = recursive_min_distance(x_right, y_right)
    delta = min(delta_left, delta_right)
    delta_strip = strip_min_distance(x_pts, y_pts, delta)

    return min(delta, delta_strip)


def strip_min_distance(x_pts, y_pts, delta):
    num = len(x_pts)
    mid = x_pts[num//2].x

    strip = [pt for pt in y_pts if mid - delta <= pt.x <= mid + delta]

    min_delta = delta
    num = len(strip)

    for i in range(num - 1):
        for j in range(i + 1, min(i + 7, num)):
            distance = euclidian_distance(*strip[i], *strip[j])
            if distance <= min_delta:
                min_delta = distance

    return min_delta


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
