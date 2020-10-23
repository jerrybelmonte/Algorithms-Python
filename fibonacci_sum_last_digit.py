# Last Digit of the Sum of Fibonacci Numbers
# Author: jerrybelmonte
# Input: Single integer n.
# Output: The last digit of the sum of F0 + F1 +...+ Fn.


def fibonacci_sum_last_digit(n: int):
    """
    Finds the last digit of a sum of the first n Fibonacci numbers.

    :param n: the number of Fibonacci numbers
    :return: the last digit of the sum

    Example 1: F0 + F1 + F3 = 0 + 1 + 1 + 2 = 4
    >>> fibonacci_sum_last_digit(3)
    4

    Example 2: Sum = 927,372,692,193,078,999,175
    >>> fibonacci_sum_last_digit(100)
    5
    """
    digit = n % 60  # the Pisano period for the fibonacci sum is 60

    if digit < 2:
        return digit

    fibonacci = [0, 1]  # holds the last digit of the fibonacci sum

    for i in range(2, digit + 1):
        last_digit = (fibonacci[i - 1] + fibonacci[i - 2]) % 10
        fibonacci.append(last_digit)

    return sum(fibonacci) % 10


if __name__ == '__main__':
    print(fibonacci_sum_last_digit(int(input())))
