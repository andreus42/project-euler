# p7: 10001st prime
# https://projecteuler.net/problem=6
# 8-6-2018, 7:30am-7:46am (v1)
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

from myMathFunc import *

n = 10001
num_prime = 10001
prime_count = 0
highest_prime = 1

while prime_count < num_prime: #starting on second prime, 3
    if is_prime(n):
        prime_count += 1
        highest_prime = n
        # print(highest_prime)
    n += 2

print(highest_prime)
