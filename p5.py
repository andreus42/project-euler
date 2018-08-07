# Andrew MetellProblem
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Only numbers under 20, excluding their prime factors, need to be checked (i.e. 19, 18, 17, 16, 15, 14, 13, 12, 11)
# Start with 2520 as it is given in the problem as the first number divisible by 1 to 10. Increment in 20s.

import numpy as np
import time

# Test contents
# current = 10
# mylist = (9, 8, 7, 6, 5)

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed

current = 2520
mylist = (19, 18, 17, 16, 15, 14, 13, 12, 11)
array_length = len(mylist)
myarray = np.asarray(mylist)

@timeit
def divisible_in_range(n):
    for x in range(0, array_length): # set to 9 after testing
        while x < array_length and current % myarray[x]==0:
            # print(myarray[x])
            x += 1

        if x == array_length:
            return 1
        else:
            return 0

while not divisible_in_range(current):
    current+=20
    # print(current)

print(current)
