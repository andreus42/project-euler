# p10: Sum of 2 million primes
# https://projecteuler.net/problem=10
# 8-7-2018, 3:00pm - 8-10-2018 10:0pm (v1)
"""
Find the sum of the first 2 million primes
(Find sum of n-million primes)
"""

import time
start = time.time()

n = 50100

numlist = list(range(3,n,2))
newlist = []
primes = [2, 3]

x = 3
while len(numlist) != 0:

    for num in numlist:
        if num % x != 0:
            newlist.append(num)

    numlist = newlist
    newlist = []

    if len(numlist) != 0:
        primes.append(numlist[0])
        x = numlist[0]

print(sum(primes))

print(f'Answer of problem 10: {num} in {time.time()-start} second(s)')
