# Algorithms in Python
Programming challenges and algorithm implementations in Python 3.

## Table of Contents
* [Objective](#objective)
* [Programming Challenges](#programming-challenges)
  - [Maximum Pairwise Product](#maximum-pairwise-product)
  - [Fibonacci Number](#fibonacci-number)
  - [Fibonacci Last Digit](#fibonacci-last-digit)
  - [Greatest Common Divisor](#greatest-common-divisor)
  - [Least Common Multiple](#least-common-multiple)
  - [Fibonacci Huge Number](#fibonacci-huge-number)
  - [Fibonacci Sum Last Digit](#fibonacci-sum-last-digit)
  - [Fibonacci Partial Sum Last Digit](#fibonacci-partial-sum-last-digit)
  - [Fibonacci Sum Of Squares Last Digit](#fibonacci-sum-of-squares-last-digit)
* [Greedy Algorithms](#greedy-algorithms)
  - [Money Change](#money-change)
  - [Fractional Knapsack](#fractional-knapsack)
  - [Car Fueling](#car-fueling)
  - [Maximum Dot Product](#maximum-dot-product)
  - [Covering Segments By Points](#covering-segments-by-points)
  - [Maximum Number Of Prizes](#maximum-number-of-prizes)
  - [Maximum Salary](#maximum-salary)
* [Divide and Conquer](#divide-and-conquer)
  - [Binary Search](#binary-search)
  - [Majority Element](#majority-element)
  - [3 Way Partition Quicksort](#3-way-partition-quicksort)
  - [Number Of Inversions](#number-of-inversions)
* [Dynamic Programming](#dynamic-programming)

## Objective
Practice implementing various algorithms in Python and gain experience designing algorithms.

## Programming Challenges

### Maximum Pairwise Product
Find the maximum product of two distinct numbers in a sequence of non-negative integers.  
**Input:** A sequence of non-negative integers _(2 ≤ n ≤ 2*10E5)_.  
**Output:** The maximum value that can be obtained by multiplying two different elements from the sequence 
_(0 ≤ a1,...,an ≤ 2*10E5)_.  
[Solution](max_pairwise_product.py "max_pairwise_product.py")

### Fibonacci Number
Given an integer n, find the nth Fibonacci number 𝐹𝑛.  
**Input:** Single integer n _(0 ≤ n ≤ 45)_.  
**Output:** nth Fibonacci number.  
[Solution](fibonacci.py "fibonacci.py")

### Fibonacci Last Digit
Given an integer n, find the last digit of the nth Fibonacci number 𝐹𝑛.  
**Input:** Single integer n _(0 ≤ n ≤ 10E7)_.  
**Output:** Last digit of Fn _(where digit is Fn mod 10)_.  
[Solution](fibonacci_last_digit.py "fibonacci_last_digit.py")

### Greatest Common Divisor
Given two integers a and b, find their greatest common divisor.  
**Input:** Two integers a and b seperated by a space _(1 ≤ a, b ≤ 2*10E9)_.  
**Output:** Greatest common divisor of a and b.  
[Solution](gcd.py "gcd.py")

### Least Common Multiple
Given two integers a and b, find their least common multiple.  
**Input:** Two integers a and b seperated by a space _(1 ≤ a, b ≤ 2*10E7)_.  
**Output:** Least common multiple of a and b.  
[Solution](lcm.py "lcm.py")

### Fibonacci Huge Number
Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod m.  
**Input:** Two integers 𝑛 and 𝑚 separated by a space. _(1 ≤ 𝑛 ≤ 10E14; 2 ≤ 𝑚 ≤ 10E3)_.  
**Output:** 𝐹𝑛 mod 𝑚.  
[Solution](fibonacci_huge.py "fibonacci_huge.py")

### Fibonacci Sum Last Digit
Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 +···+ 𝐹𝑛.  
**Input:** Single integer 𝑛 _(0 ≤ 𝑛 ≤ 10E14)_.  
**Output:** The last digit of 𝐹0 + 𝐹1 +···+ 𝐹𝑛.  
[Solution](fibonacci_sum_last_digit.py "fibonacci_sum_last_digit.py")

### Fibonacci Partial Sum Last Digit
Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 +···+ 𝐹𝑛.  
**Input:** Two non-negative integers 𝑚 and 𝑛 separated by a space _(0 ≤ 𝑚 ≤ 𝑛 ≤ 10E14)_.  
**Output:** The last digit of 𝐹𝑚 + 𝐹𝑚+1 +···+ 𝐹𝑛.  
[Solution](fibonacci_partial_sum.py "fibonacci_partial_sum.py")

### Fibonacci Sum Of Squares Last Digit
Compute the last digit of 𝐹0^2 + 𝐹1^2 +···+ 𝐹𝑛^2.  
**Input:** Integer 𝑛 _(0 ≤ 𝑛 ≤ 10E14)_.  
**Output:** The last digit of 𝐹0^2 + 𝐹1^2 +···+ 𝐹𝑛^2.  
[Solution](fibonacci_sum_squares.py "fibonacci_sum_squares.py")


## Greedy Algorithms

### Money Change
Goal is to find the minimum number of coins needed to change the input value into coins with denominations 1, 5, and 10.  
**Input:** Single integer 𝑚 _(1 ≤ 𝑚 ≤ 10E3)_.  
**Output:** The minimum number of coins with denominations 1, 5, 10 that changes 𝑚.  
[Solution](change.py "change.py")

### Fractional Knapsack
Implement an algorithm for the fractional knapsack problem.  
**Input:** First line contains the number 𝑛 of items and the capacity W of a knapsack. Following 𝑛 lines define the 
values and the weights of the items. The i-th line contains integers 𝑣𝑖 and 𝑤𝑖, the value and weight of the i-th item, 
respectively _(1 ≤ 𝑛 ≤ 10E3, 0 ≤ 𝑊 ≤ 2·10E6; 0 ≤ 𝑣𝑖 ≤ 2·10E6, 0 < 𝑤𝑖 ≤2·10E6 for all 1 ≤ 𝑖 ≤ 𝑛)_.  
**Output:** The maximal value of fractions of items that fit into the knapsack. The output has to have at least four 
digits after the decimal point.  
[Solution](fractional_knapsack.py "fractional_knapsack.py")

### Car Fueling
What is the minimum number of refills needed to travel to another city located 𝑑 miles away. The car starts with a full 
tank and can travel 𝑚 miles on a full tank. Along the journey there are gas stations at distances stop1, stop2,..., stop𝑛.  
**Input:** Firt line contains an integer 𝑑. Second line contains an integer 𝑚. The third line specifies an integer 𝑛. 
The last line contains integers stop1, stop2,..., stop𝑛 _(1 ≤ 𝑑 ≤ 10E5; 1 ≤ 𝑚 ≤ 400; 1 ≤ 𝑛 ≤ 300; 0 < stop1 < stop2 
<···< stop𝑛 < 𝑑)_.  
**Output:** The minimum number of refills needed, assuming the car starts with a full tank. If it is not possible to 
reach the destination, output -1.  
[Solution](car_fueling.py "car_fueling.py")

### Maximum Dot Product
Given two sequences 𝑎1,𝑎2,...,𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad) and 𝑏1,𝑏2,...,𝑏𝑛 (𝑏𝑖 is the average number of 
clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎𝑖,𝑏𝑗) such that the sum of their products is 
maximized.  
**Input:** The first line contains an integer 𝑛, the second one contains a sequence of integers 𝑎1,𝑎2,...,𝑎𝑛, the third 
one contains a sequence of integers 𝑏1,𝑏2,...,𝑏𝑛 _(1 ≤ 𝑛 ≤ 10E3; −10E5 ≤ 𝑎𝑖,𝑏𝑖 ≤ 10E5 for all 1 ≤ 𝑖 ≤ 𝑛)_.  
**Output:** The maximum value of ∑︀ 𝑎𝑖𝑐𝑖, where 𝑐1,𝑐2,...,𝑐𝑛 is a permutation of 𝑏1,𝑏2,...,𝑏𝑛.  
[Solution](dot_product.py "dot_product.py")

### Covering Segments By Points
Given a set of 𝑛 segments {(𝑎0,𝑏0),(𝑎1,𝑏1),...,(𝑎𝑛−1,𝑏𝑛−1)} with integer coordinates on a line, find the minimum number 𝑚 
of points such that each segment contains at least one point. That is, find a set of integers 𝑋 of the minimum size such 
that for any segment (𝑎𝑖,𝑏𝑖) there is a point 𝑥 ∈ 𝑋 such that 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.  
**Input:** The first line of the input contains the number 𝑛 of segments. Each of the following 𝑛 lines contains two 
integers 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th segment _(1 ≤ 𝑛 ≤ 100; 0 ≤ 𝑎𝑖 
≤ 𝑏𝑖 ≤ 10E9 for all 0 ≤ 𝑖 < 𝑛)_.  
**Output:** The minimum number 𝑚 of points on the first line and the integer coordinates of 𝑚 points (separated by 
spaces) on the second line.  
[Solution](covering_segments.py "covering_segments.py")

### Maximum Number Of Prizes
The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise distinct positive 
integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as 𝑎1+𝑎2+···+𝑎𝑘 where 𝑎1,...,𝑎𝑘 are 
positive integers and 𝑎𝑖 != 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.  
**Input:** A single integer n _(1 ≤ 𝑛 ≤ 10E9)_.  
**Output:** In the first line, output the maximum number 𝑘 such that 𝑛 can be represented as a sum of 𝑘 pairwise distinct 
positive integers. In the second line, output 𝑘 pairwise distinct positive integers that sum up to 𝑛 (if they exist).  
[Solution](different_summands.py "different_summands.py")

### Maximum Salary
The goal is to composes the largest number out of a set of integers.  
**Input:** First line contains an integer n. Second line contains integers separated by a space _(1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑎𝑖 ≤ 
10E3 for all 1 ≤ 𝑖 ≤ 𝑛)_.  
**Output:** The largest number that can be composed out of a1,a2,...,an.  
[Solution](largest_number.py "largest_number.py")


## Divide and Conquer

### Binary Search
The goal is to implement the binary search algorithm.  
**Input:** The first line of the input contains an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1 of 𝑛 pairwise distinct 
positive integers in increasing order. The next line contains an integer 𝑘 and 𝑘 positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1 
_(1 ≤ 𝑘 ≤ 10E5; 1 ≤ 𝑛 ≤ 3·10E4; 1 ≤ 𝑎𝑖 ≤10E9 for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏𝑗 ≤ 10E9 for all 0 ≤ 𝑗 < 𝑘)_.  
**Output:** For all 𝑖 from 0 to 𝑘−1, output an index 0 ≤ 𝑗 ≤ 𝑛−1 such that 𝑎𝑗 = 𝑏𝑖 or −1 if there is no such index.  
[Solution](binary_search.py "binary_search.py")

### Majority Element
Check whether an input sequence contains a majority element.  
**Input:** The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative integers 𝑎0,𝑎1,...,𝑎𝑛−1 
_(1 ≤ 𝑛 ≤ 10E5; 0 ≤ 𝑎𝑖 ≤ 10E9 for all 0 ≤ 𝑖 < 𝑛)_.  
**Output:** 1 if the sequence contains an element that appears strictly more than 𝑛/2 times, and 0 otherwise.  
[Solution](majority_element.py "majority_element.py")

### 3 Way Partition Quicksort
Implement the quicksort algorithm to efficiently process a sequences with few unique elements, by implementing a 3-way 
partition of the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.  
**Input:** The first line of the input contains an integer 𝑛. The next line contains a sequence of 𝑛 integers 𝑎0,𝑎1,...,𝑎𝑛−1 
_(1 ≤ 𝑛 ≤ 10E5; 1 ≤ 𝑎𝑖 ≤ 10E9 for all 0 ≤ 𝑖 < 𝑛)_.  
**Output:** The sorted sequence in non-decreasing order.  
[Solution](sorting.py "sorting.py")

### Number Of Inversions
Count the number of inversions of a given sequence.  
**Input:** The first line contains an integer 𝑛, the next one contains a sequence of integers 𝑎0,𝑎1,...,𝑎𝑛−1 
_(1 ≤ 𝑛 ≤ 10E5, 1 ≤ 𝑎𝑖 ≤ 10E9 for all 0 ≤ 𝑖 < 𝑛)_.  
**Output:** Integer of the inversions in the sequence.  
[Solution](inversions.py "inversions.py")

### Organizing A Loterry
[Solution](points_and_segments.py "points_and_segments.py")

### Closest Points
[Solution](closest.py "closest.py")

## Dynamic Programming

## Technologies
Python 3.8
