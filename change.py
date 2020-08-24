# Uses python3
def get_change(m):
    min_coins = 0
    while m >= 10:
        min_coins += 1
        m -= 10
    while m >= 5:
        min_coins += 1
        m -= 5
    while m > 0:
        min_coins += 1
        m -= 1
    return min_coins


if __name__ == '__main__':
    m_ = int(input())
    print(get_change(m_))
