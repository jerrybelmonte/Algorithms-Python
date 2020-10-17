# Maximum Pairwise Product
# Author: jerrybelmonte
# Input: First line contains an integer n (2 <= n <= 2*10E5). Second line
# contains n non-negative integers (0 <= a1,...,an <= 2*10E5).
# Output: Integer of the maximum pairwise product.


def maximum_pairwise_product(numbers):
    # sorting in descending order is O(n*logn)
    numbers.sort(reverse=True)
    # the first two numbers will produce the largest product
    return numbers[0] * numbers[1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(num) for num in input().split()]
    print(maximum_pairwise_product(input_numbers))
