# p10: Sum of 2 million primes (v3)
# https://projecteuler.net/problem=10
# 8-10-2018, 10:15am
"""
Find the sum of the first 2 million primes
(Find sum of n-million primes)
Using the Sieve of Eratosthenes
"""
#
import time
import math

start = time.time()

n = 2000000
numlist = [True] * n
numlist[0]=False
numlist[1]=False
count = 2 # counting twos, could be omitted but makes complete prime list
crosslimit = math.sqrt(n)

# Count up to sqrt(n) {the largest prime in n}, set composites false in loop
while count < crosslimit:
    if numlist[count]: # (number index is true)
        for num in range(count+count, n, count):
            numlist[num] = False
    count += 1

# Loop through boolean array and add up primes
def sumlist(l):
    sum = 0
    for num in range(1, len(numlist), 2):
        if numlist[num] == True:
            sum += num
    return(sum)

print(f'Answer of problem 10: {sumlist(numlist)} in {time.time()-start} second(s)')
