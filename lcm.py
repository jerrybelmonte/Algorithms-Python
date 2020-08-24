# Uses python3
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd(a, b):
    left, right = max(a, b), min(a, b)
    if right == 0:
        return left
    left, right = right, left % right
    return gcd(left, right)


def lcm(a, b):
    return (a//gcd(a, b))*b


if __name__ == '__main__':
    a_val, b_val = input().split()
    print(lcm(int(a_val), int(b_val)))

