# p3: Largest prime factor
# What is the largest prime factor of the number 600851475143 ?
# https://projecteuler.net/problem=3
# 8-5-2018, 9:27am (20 minutes)

import math
import time
start = time.time()

i = 0

num=600851475143
max=math.ceil(math.sqrt(num))
# print(f'Max: {max}')

def is_prime(num):
    for n in range((num-1),1,-1):
        if num%n==0:
            return 0
    return 1

largest_prime=1

for n in range(1, max, 2):
    if num%n==0 and is_prime(n):
        largest_prime=n
    i+=1

answer = largest_prime

print(f'Answer of problem 7: {answer}')
print(f'In {time.time()-start} second(s)')
print(f'With {i} iterations')
