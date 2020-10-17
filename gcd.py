# Greatest Common Divisor
# Author: jerrybelmonte
# Input: Two integers a and by seperated by a space.
# Output: Greatest common divisor of a and b.
# Implements the Euclidean algorithm for computing the
# greatest common divisor.


def gcd(a, b):
    # left >= right, ensures descending numbers
    left, right = max(a, b), min(a, b)

    if right == 0:  # base case
        return left  # left is the greatest common divisor

    # keep dividing until remainder is 0
    return gcd(right, (left % right))


if __name__ == "__main__":
    a, b = input().split()
    print(gcd(int(a), int(b)))
