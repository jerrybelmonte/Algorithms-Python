# Maximum Salary
# Author: jerrybelmonte
# Input: First line contains an integer n.
# Second line contains integers separated by a space.
# Output: The largest number that can be composed out of a1,a2,...,an.
import sys


def greater_or_equal(d: str, m: str):
    """
    Checks if the digit is greater or equal than the max digit.

    :param d: the current digit
    :param m: the max digit
    :return: True if d >= m

    >>> greater_or_equal('2', '21')
    True

    >>> greater_or_equal('21', '2')
    False

    >>> greater_or_equal('33', '3')
    True

    >>> greater_or_equal('3', '33')
    True
    """
    digit_max, max_digit = d + m, m + d
    left, right = int(digit_max), int(max_digit)
    return left >= right


def largest_number(digits: list):
    """
    Composes the largest number out of a set of integers.

    :param digits: the set of numbers
    :return: the largest number that can be composed

    >>> largest_number(['2', '3', '9'])
    '932'

    >>> largest_number(['21', '2'])
    '221'

    >>> largest_number(['2', '21'])
    '221'

    >>> largest_number(['9', '4', '6', '1', '9'])
    '99641'

    >>> largest_number(['9', '4', '6', '10', '9'])
    '996410'

    >>> largest_number(['23', '39', '92'])
    '923923'

    >>> largest_number(['6', '61', '68'])
    '68661'

    >>> largest_number(['4', '42', '46', '427', '465'])
    '46546442742'

    >>> largest_number(['5', '52', '57', '517', '532', '569', '581'])
    '58157569553252517'
    """
    res = ""

    while digits:
        max_digit = ''

        for i in range(len(digits)):
            if greater_or_equal(digits[i], max_digit):
                max_digit = digits[i]

        res += max_digit
        digits.remove(max_digit)

    return res


if __name__ == '__main__':
    data = sys.stdin.read().split()
    a = data[1:]
    print(largest_number(a))
