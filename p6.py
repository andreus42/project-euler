# p6: Sum square difference
# The sum of the squares of the first ten natural numbers is,
# https://projecteuler.net/problem=6
# 8-6-2018, 5:50am-6:09am
"""
The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

SquareOfSums = sum([x for x in range(1,101)])**2
SumOfSquares = sum([x**2 for x in range(1,101)])
print(SquareOfSums-SumOfSquares)
