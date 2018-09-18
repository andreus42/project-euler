# Andrew MetellProblem
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Only numbers under 20, excluding their prime factors, need to be checked (i.e. 19, 18, 17, 16, 15, 14, 13, 12, 11)
# Start with 2520 as it is given in the problem as the first number divisible by 1 to 10. Increment in 20s.

import numpy as np
import time

start = time.time()
iter=0
current = 2520
mylist = (19, 18, 17, 16, 15, 14, 13, 12, 11)
array_length = len(mylist)
myarray = np.asarray(mylist)

def divisible_in_range(n):
    for x in range(0, array_length): # set to 9 after testing
        while x < array_length and current % myarray[x]==0:
            x += 1

        if x == array_length:
            return 1
        else:
            return 0


while not divisible_in_range(current):
    current+=20

answer = current

print(f'Answer of problem 7: {answer}')
print(f'In {time.time()-start} second(s)')
print(f'With {iter} iterations')
