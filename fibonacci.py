# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    def calc_fib_nums(num, m):
        n_val = str(num)
        if n_val in m:
            return m.get(n_val)
        m[n_val] = calc_fib_nums(num - 1, m) + calc_fib_nums(num - 2, m)
        return m.get(n_val)

    fib_nums = {'1': 1, '0': 0}
    return calc_fib_nums(n, fib_nums)


n = int(input())
print(calc_fib(n))
