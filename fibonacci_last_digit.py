# Uses python3
def get_fibonacci_last_digit_naive(num):
    if num <= 1:
        return num

    previous = 0
    current = 1

    for _ in range(num - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit(num):
    if num <= 1:
        return num
    fib = {'0': 0, '1': 1}
    for i in range(2, num + 1):
        cur = str(i - 1)
        prev = str(i - 2)
        fib[str(i)] = (fib.get(cur) + fib.get(prev)) % 10
    return fib.get(str(num))


if __name__ == '__main__':
    n_ = int(input())
    print(get_fibonacci_last_digit(n_))
