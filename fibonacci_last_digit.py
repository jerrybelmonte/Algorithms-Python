# Last Digit of a Large Fibonacci Number
# Author: jerrybelmonte
# Input: Single integer n.
# Output: Last digit of Fn.


def get_fibonacci_last_digit(num):
    if num <= 1:  # base case
        return num
    
    # implement a fibonacci lookup table for the last digit
    fib_dict = {'0': 0, '1': 1}

    # stores the last digit instead of the Fibonacci number
    for i in range(2, num + 1):
        cur = str(i - 1)  # current last digit in the Fibonacci sequence
        prev = str(i - 2) # previous last digit in the Fibonacci sequence

        # f[i] is the last digit of the sum of the last digits of
        # f[i - 1] + f[i - 2], which has a better memory performance
        fib_dict[str(i)] = (fib_dict.get(cur) + fib_dict.get(prev)) % 10

    return fib_dict.get(str(num))


if __name__ == '__main__':
    print(get_fibonacci_last_digit(int(input())))
