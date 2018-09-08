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


def next_triangle_numbers(count, value):
    count += 1
    value += count
    return(count, value)

def divisors_count(n):
    count = 0
    for num in range (1,round(math.sqrt(n))+1):
        if n % num == 0:
            count += 2
    return(count)

triangle_number = [0, 0]

highest_divisor_count = 0
i = 0
while highest_divisor_count < 500:
    triangle_number = next_triangle_numbers(triangle_number[0], triangle_number[1])
    # print(f'Next Triangle Number: {triangle_number}')
    local_divisor_count = divisors_count(triangle_number[1])
    print(f'Local Divisor Count: {local_divisor_count}, triangle_number {triangle_number} at {time.time()-start} second(s)')
    i += 1
    if local_divisor_count > highest_divisor_count:
        highest_divisor_count = local_divisor_count

print(f'triangle_number: {triangle_number}')
print(f'Highest Divisor Count:{highest_divisor_count}')

# for number in range(0,10):
#     print(triangle_numbers(number))

print(f'Clocked in at {time.time()-start} second(s)')
