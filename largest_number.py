# Uses python3
import sys


def greater_or_equal(d, m):
    left, right = list(d), list(m)
    for x in left:
        j = 0
        while j < len(right):
            if x >= right[j]:
                j += 1
            else:
                return False
    return True


def largest_number(digits):
    res = ""

    while len(digits) > 0:
        max_digit = max(digits)

        for digit in digits:
            if greater_or_equal(digit, max_digit):
                max_digit = digit

        res += max_digit
        digits.remove(max_digit)

    return res


if __name__ == '__main__':
    input_ = sys.stdin.read()
    data = input_.split()
    a_ = data[1:]
    print(largest_number(a_))
    # print('932 =', '932' == largest_number(['2', '3', '9']))
    # print(largest_number(['21', '2']))
    # print(largest_number(['2', '21']))
    # print(largest_number(['9', '4', '6', '1', '9']))
    # print(largest_number(['9', '4', '6', '10', '9']))
    # print(largest_number(['23', '39', '92']))
    # print(largest_number(['92', '39', '23']))
    # print('68661 =', '68661' == largest_number(['6', '61', '68']))
    # print('46546442742 =', largest_number(['4', '42', '46', '427', '465']))
    # print('58157569553252517 =', '58157569553252517' == largest_number(['5', '52', '57', '517', '532', '569', '581']))
