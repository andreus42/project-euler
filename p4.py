# p4: Largest palindrome product
# What is the largest prime factor of the number 600851475143 ?
# https://projecteuler.net/problem=4
# 8-5-2018, 9:43pm-10:27pm

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers
"""

import time
start = time.time()

def is_palindrome(num):
    num_str=str(num)
    return num_str[::-1]==num_str

myList = []

for n in range(100,999):
    for x in range(100,999):
        myList.append(x*n)

answer = sorted(myList, reverse=True)

for num in answer:
    if is_palindrome(num):
        # print(num)
        break

print(f'Answer of problem 7: {num} in {time.time()-start} second(s)')
