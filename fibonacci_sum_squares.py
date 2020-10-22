# Last Digit of the Sum of Squares of Fibonacci Numbers
# Author: jerrybelmonte
# Input: Single integer n.
# Output: The last digit of F0^2 + F1^2 +...+ Fn^2.


def fibonacci_sum_squares(n: int):
    """
    Computes the last digit of F0^2 + F1^2 + ... + Fn^2.

    :param n: the sequence size of Fibonacci numbers
    :return: the last digit of the sum of squares

    Example 1:
    0+1+1+4+9+25+64+169=273
    >>>fibonacci_sum_squares(7)
    >>>3

    Example 2:
    F73 = 1,052,478,208,141,359,608,061,842,155,201
    >>>fibonacci_sum_squares(73)
    >>>1
    """
    n %= 60

    if n < 2:
        return n

    fibonacci = [0, 1]
    fibonacci_sq_sum = 0

    for i in range(2, n + 1):
        last_digit = (fibonacci[i - 1] + fibonacci[i - 2]) % 10
        fibonacci.append(last_digit)

    for num in fibonacci:
        fibonacci_sq_sum += num**2 % 10
        fibonacci_sq_sum %= 10

    return fibonacci_sq_sum


if __name__ == '__main__':
    print(fibonacci_sum_squares(int(input())))
