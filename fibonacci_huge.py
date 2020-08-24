# Uses python3
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    fib = {'0': 0, '1': 1}
    pisano = 3
    if m > 2:
        i = 2
        p = 0
        c = 0
        while (p, c) != (0, 1):
            fib[str(i)] = (fib.get(str(i-1)) + fib.get(str(i-2)))
            p = (fib.get(str(i-1)) % m)
            c = (fib.get(str(i)) % m)
            i += 1
        pisano = i - 2

    rem = str(n % pisano)
    if rem not in fib:
        for i in range(len(fib), rem + 1):
            fib[str(i)] = (fib.get(str(i-1)) + fib.get(str(i-2)))

    fib_num = fib.get(rem)
    return fib_num % m


if __name__ == '__main__':
    n_, m_ = input().split()
    print(get_fibonacci_huge(int(n_), int(m_)))
