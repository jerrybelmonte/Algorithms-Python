# Least Common Multiple
# Author: jerrybelmonte
# Input: Two integers a and b seperated by a space.
# Output: Least common multiple of a and b.
# Uses the Euclidean algorithm of the greatest common divisor
# to compute the least common multiple.


def lcm(a, b):
    # greatest common divisor helper function
    def gcd(a, b):
        left, right = max(a, b), min(a, b)

        if right == 0:  # base case
            return left  # left is the greatest common divisor

        # recursively call the gcd function
        return gcd(right, (left % right))

    # return the least common multiple
    return (a // gcd(a, b)) * b


if __name__ == '__main__':
    a, b = input().split()
    print(lcm(int(a), int(b)))
