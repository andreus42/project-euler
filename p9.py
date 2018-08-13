# p9: Special Pythagorean triplet
# https://projecteuler.net/problem=9
# 8-6-2018, 10:46pm-, (v1)
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

a = 1
b = 1
c = 1

for n in range(333,1,-1):
    # print(n)
    a = n
    for m in range(1000,1,-1):
        b = m
        c = math.sqrt(a**2 + b**2)
        # print(a, b, c)
        if a + b + c == 1000:
            print(f'a: {a}, b: {b}, c: {c}, a * b * c: {a * b * c}')
