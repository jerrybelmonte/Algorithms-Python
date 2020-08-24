# Uses python3
def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum_sq = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum_sq += current * current

    return sum_sq % 10


def fibonacci_sum_squares(n):
    n %= 60

    if n < 2:
        return n

    fib = [0, 1]
    fsum = 0

    for i in range(2, n + 1):
        num = (fib[i - 1] + fib[i - 2]) % 10
        fib.append(num)

    for num in fib:
        fsum += (num * num) % 10
        fsum %= 10

    return fsum


if __name__ == '__main__':
    n_ = input()
    print(fibonacci_sum_squares(int(n_)))
