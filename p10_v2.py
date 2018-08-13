# p10: Sum of 2 million primes 
# https://projecteuler.net/problem=10
# 8-10-2018, 10:00pm - 8-10-2018 10:10am (v2)
"""
Find the sum of the first 2 million primes
(Find sum of n-million primes)
"""
#
import time
start = time.time()

n = 50100
sum = 0
count = 2
numlist = [True] * n
numlist[0]=False
numlist[1]=False

while count < n:

    if numlist[count]: # (number index is true)
        for num in range(count+count, n, count):
            numlist[num] = False

    count += 1

for num in range(1, len(numlist)):
    if numlist[num] == True:
        sum += num

print(f'Answer of problem 10: {sum} in {time.time()-start} second(s)')
