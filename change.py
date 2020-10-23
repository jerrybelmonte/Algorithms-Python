# Money Change
# Author: jerrybelmonte
# Input: Integer m of the money given.
# Output: The minimum number of coins with denominations 1, 5, and 10.


def get_change(money: int):
    """
    Greggy implementation used by cashiers for getting change.

    :param money: the amount we need change for
    :return: the minimum number of coins
    """
    min_coins = 0

    while money >= 10:
        min_coins += 1
        money -= 10

    while money >= 5:
        min_coins += 1
        money -= 5

    while money > 0:
        min_coins += 1
        money -= 1

    return min_coins


if __name__ == '__main__':
    print(get_change(int(input())))
