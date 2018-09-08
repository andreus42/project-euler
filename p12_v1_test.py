"""# p11: Triangle Number divisors.
# https://projecteuler.net/problem=12
# 9-2-2018, 11:16pm-

Find the first triangle number that has more than 500 divisors:
A triangle number is a the sum natural numbers up to that numbers.
For example the 5th triangle number is 15 (1+2+3+4+5)
---
Visualized next rev using a triangle_number object: Triangle(num, value)

Psuedo Code
1. Make Triangle Number Generator
2. Make Divisor Number Counter
3. Loop through numbers to find one with more than 500 divisors
"""
# Timing Tools
import time
import math
start = time.time()

#  Original Triangle Number Function
# def triangle_numbers(x):
#     count = 0
#     value = 0
#     for number in range (1,x+1):
#         count += 1 # count of triangle number
#         value += number # value of triangele number
#     return(count, value)


# Number of divisors
def divisors_count(n):
    """Use strategy similiar to sieve of ErastophanesCheck
    1. Make an array of boolenas from 0 to n.
    2. Check upto sqrt of n.
       2a. When a divisor is found, check off higher divisors in n.
    3. Sum marked divisors in array
    """

    # Make an array of booleans up to n
    # numlist = [False] * n
    # # numlist[0]=False
    # numlist[1]=True
    #
    # # Count up to sqrt(n) {the largest prime in n}. Larger composites will be marked
    # # Set composites to true in loop
    # while count < crosslimit:
    #     # If number is not yet found as composite, mark it and all larger numbers
    #     # divisible by it.
    #     if numlist[count] != True: # (number index is true)
    #         for num in range(count, n):
    #             numlist[num] = True
    #     count += 1
    #
    # # Loop through boolean array and add up composites
    # def sumlist(l):
    #     sum = 0
    #     for num in range(1, n):
    #         if numlist[num] == True:
    #             sum += num
    #     return(sum)

def next_triangle_number(count, value):
    count += 1
    value += count
    return(count, value)

triangle_number = [1, 1]

# i = 0
# while triangle_number[0] < 10000000:
#     triangle_number = next_triangle_number(triangle_number[0], triangle_number[1])
#     print(triangle_number)
#     i += 1

print(f'Divisor of {triangle_number} is {divisors_count(triangle_number[1])}')

highest_divisor_count = 0
i = 0
while highest_divisor_count < 144:
    triangle_number = next_triangle_number(triangle_number[0], triangle_number[1])
    # print(f'Next Triangle Number: {triangle_number}')
    local_divisor_count = divisors_count(triangle_number[1])
    # print(f'Divsors of {triangle_number[1]}: {local_divisor_count}')
    i += 1
    if local_divisor_count > highest_divisor_count:
        print(f'Local Divisor Count: {local_divisor_count}, triangle_number {triangle_number} at {time.time()-start} second(s)')
        highest_divisor_count = local_divisor_count

print(f'triangle_number: {triangle_number}')
print(f'Highest Divisor Count:{highest_divisor_count}')

# for number in range(0,10):
#     print(triangle_numbers(number))

print(f'Clocked in at {time.time()-start} second(s)')
