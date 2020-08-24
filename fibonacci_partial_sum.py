# Uses python3
def fibonacci_partial_sum_naive(from_i, to_i):
    psum = 0
    current = 0
    next_s = 1

    for i in range(to_i + 1):
        if i >= from_i:
            psum += current

        current, next_s = next_s, current + next_s

    return psum % 10


def fibonacci_partial_sum(m, n):
    fib = [0, 1]
    if m == n:
        num = n % 60
        if num <= 1:
            return num
        for i in range(2, num + 1):
            fib.append(((fib[i - 1] + fib[i - 2]) % 10))
        return fib[num]
    start_ndx = m % 60
    end_ndx = n % 60 + 1
    if start_ndx >= end_ndx:
        end_ndx += 60
    for i in range(2, end_ndx):
        fib.append(((fib[i - 1] + fib[i - 2]) % 10))
    return sum(fib[start_ndx:end_ndx]) % 10


if __name__ == '__main__':
    from_, to_ = input().split()
    # print('Naive:', fibonacci_partial_sum_naive(int(from_), int(to_)))
    print(fibonacci_partial_sum(int(from_), int(to_)))
