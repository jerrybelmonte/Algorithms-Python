# Maximum Number of Prizes (Different Summands)
# Author: jerrybelmonte
# Input: Single integer n.
# Output: First line is the maximum number k of integers.
# Followed by the distinct integers that sum up to n.


def optimal_summands(n: int):
    """
    Gets the maximum number of distinct prizes.

    >>> optimal_summands(6)
    [1, 2, 3]

    >>> optimal_summands(8)
    [1, 2, 5]

    >>> optimal_summands(2)
    [2]
    """
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
            summands[-1] += n - (opt_sum - num)
            break

    return summands


if __name__ == '__main__':
    res = optimal_summands(int(input()))
    print(len(res))
    for x in res:
        print(x, end=' ')
