# Uses python3
def optimal_summands(n):
    if n <= 2:
        return [n]

    opt_sum = 0
    summands = []

    for num in range(1, n):
        opt_sum += num

        if opt_sum < n:
            summands.append(num)
        elif opt_sum == n:
            summands.append(num)
            break
        else:
            diff = n - (opt_sum - num)
            summands[-1] += diff
            break

    return summands


if __name__ == '__main__':
    n_ = int(input())
    res = optimal_summands(n_)
    print(len(res))
    for x in res:
        print(x, end=' ')
