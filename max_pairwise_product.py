# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max1 = max(numbers)
    first_ndx = 0
    for ndx in range(n):
        if numbers[ndx] == max1:
            first_ndx = ndx
            break
    max2 = 0
    if first_ndx != 0:
        max2 = numbers[0]
    else:
        max2 = numbers[1]
    for ndx in range(n):
        if ndx != first_ndx:
            max2 = max(max2, numbers[ndx])
    max_product = max1 * max2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
