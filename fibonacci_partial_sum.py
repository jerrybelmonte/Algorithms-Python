# Last Digit of the Partial Sum of Fibonacci Numbers
# Author: jerrybelmonte
# Input: Two non-negative integers m and n separated by a space.
# Output: The last digit of Fm + Fm+1 +...+ Fn.


def fibonacci_partial_sum(m: int, n: int):
    """
    Finds the lsat digit of a partial sum of Fibonacci numbers:
    Fm + Fm+1 + ... + Fn.

    :param m: starting index in Finacci sequence
    :param n: end index in Fibonacci sequence
    :return: the last digit of the partial sum

    Example: F3 + F4 + F5 + F7 = 2 + 3 + 5 + 8 + 13 = 31
    >>>fibonacci_partial_sum(3, 7)
    >>>1
    """
    pisano_period = 60
    partial_sum = [0, 1]

    if m == n:  # base case for a single fibonacci number
        fibonacci = n % pisano_period

        if fibonacci <= 1:  # base case for Fn <= 1
            return fibonacci

        for i in range(2, fibonacci + 1):  # compute the fibonacci sequence
            digit = (partial_sum[i - 1] + partial_sum[i - 2]) % 10
            partial_sum.append(digit)

        return partial_sum[fibonacci]

    start_ndx = m % pisano_period
    end_ndx = n % pisano_period + 1

    if start_ndx >= end_ndx:
        end_ndx += pisano_period

    for i in range(2, end_ndx):
        digit = (partial_sum[i - 1] + partial_sum[i - 2]) % 10
        partial_sum.append(digit)

    return sum(partial_sum[start_ndx:end_ndx]) % 10


if __name__ == '__main__':
    start, end = input().split()
    print(fibonacci_partial_sum(int(start), int(end)))
