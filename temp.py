"""Temp file for function testing"""

import math
# import time
# start = time.time()

# Number of divisors
def divisors_count(n):
    """Use strategy similiar to sieve of ErastophanesCheck
    1. Make an array of boolenas from 0 to n.
    2. Check upto sqrt of n.
       2a. When a divisor is found, check off higher divisors in n.
    3. Sum marked divisors in array
    """

    # Make an array of booleans up to n
    numlist = [False] * n
    print(numlist)
    numlist[0]=False
    numlist[1]=True
    count = 2
    crosslimit = math.sqrt(n)

    # Count up to sqrt(n) {the largest prime in n}. Larger composites will be marked
    # Set composites to true in loop
    while count < crosslimit:
        # If number is not yet found as composite, mark it and all larger numbers
        # divisible by it.
        if (numlist[count] != True) and (n % count == 0): # (number index is true)
            for num in range(count+count, n, count):
                numlist[num] = True
        count += 1

    print(numlist)

    # Loop through boolean array and add up composites
    def sumlist(l):
        sum = 0
        for num in range(1, n):
            if numlist[num] == True:
                sum += num
        return(sum)

x = 10
print(divisors_count(x))

# print(f'Clocked in at {time.time()-start} second(s)')
