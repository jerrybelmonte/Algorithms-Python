# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd(a, b):
    left, right = max(a, b), min(a, b)
    if right == 0:
        return left
    left, right = right, left % right
    return gcd(left, right)


if __name__ == "__main__":
    a_val, b_val = input().split()
    print(gcd(int(a_val), int(b_val)))
