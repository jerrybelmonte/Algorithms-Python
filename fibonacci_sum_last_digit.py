# Uses python3
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    fsum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        fsum += current

    return fsum % 10


def fibonacci_sum_last_digit(n):
    num = n % 60

    if num < 2:
        return num

    fib = [0, 1]

    for i in range(2, num + 1):
        fib.append(((fib[i - 1] + fib[i - 2]) % 10))

    return sum(fib) % 10


if __name__ == '__main__':
    n_ = int(input())
    print(fibonacci_sum_last_digit(n_))
