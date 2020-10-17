# Fibonacci Number
# Author: jerrybelmonte
# Input: Single integer n.
# Output: nth Fibonnaci number.


def get_fibonacci(n):
    if n <= 1:  # base case
        return n

    # implement a fibonnaci lookup table
    fibonacci_dict = {'0': 0, '1': 1}

    # optimize memory space by using a for loop instead of recursion
    for k in range(2, n+1):
        fib_num = fibonacci_dict[str((k-1))] + fibonacci_dict[str((k-2))]
        fibonacci_dict.setdefault(str(k), fib_num)
    
    # return the nth fibonnaci value from the dictionary
    return fibonacci_dict.get(str(n))


n = int(input())
print(get_fibonacci(n))
