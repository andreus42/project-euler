# p7: 10001st prime
# https://projecteuler.net/problem=6
# 8-6-2018, 7:30am-7:46am (v1)
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
Answer:
"""
import time
import math

start = time.time()

n = 500000
numlist = [True] * n
numlist[0]=False
numlist[1]=False

nth_prime = 10001
count = 2

# Count up to sqrt(n) {the largest prime in n}, set composites false in loop
while count < math.sqrt(n):

    if numlist[count]: # (number index is true)
        for num in range(count+count, n, count):
            numlist[num] = False
    count += 1

# Find n'th Prime in boolean list
def nth_prime(num, numlist):
    primes = 0
    count = 0
    while primes < num:
        if numlist[count]: #is True
            primes += 1
        count +=1
    return count-1

answer = nth_prime(10001, numlist)
print(f'Answer of problem 7: {answer} in {time.time()-start} second(s)')
