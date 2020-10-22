# Fibonacci Huge Number
# Author: jerrybelmonte
# Input: Two integers n and m separated by a space.
# Output: Fn mod m
# Note: For an integer m >= 2, the sequence Fn mod m is periodic.
# It is a Pisano period that always starts with 01.


def get_fibonacci_huge(n: int, m: int):
    """
    Gets the remainder of Fn when divided by m.

    :param n: nth Fibonacci number
    :param m: the divisor of Fn
    :return: Fn mod m

    Example 1:
    >>>get_fibonacci_huge(239, 1000)
    >>>161

    Example 2:
    >>>get_fibonacci_huge(2816213588, 239)
    >>>151
    """
    if n <= 1:  # base case
        return n

    fibonacci = {'0': 0, '1': 1}
    pisano = 3

    if m > 2:
        ndx = 2
        previous = 0
        current = 0

        while (previous, current) != (0, 1):
            fibonacci[str(ndx)] = (fibonacci.get(str(ndx - 1)) +
                                   fibonacci.get(str(ndx - 2)))

            previous = fibonacci.get(str(ndx - 1)) % m
            current = fibonacci.get(str(ndx)) % m
            ndx += 1

        pisano = ndx - 2

    remainder = str(n % pisano)

    if remainder not in fibonacci:
        for i in range(len(fibonacci), remainder + 1):
            fibonacci[str(i)] = (fibonacci.get(str(i - 1)) +
                                 fibonacci.get(str(i - 2)))

    return fibonacci.get(remainder) % m


if __name__ == '__main__':
    n, m = input().split()
    print(get_fibonacci_huge(int(n), int(m)))
