"""# Longest Collatz sequence
# https://projecteuler.net/problem=14
# 9-8-2018, 5:11am-

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# Timing Tools
import time
start = time.time()

largest_seq = 0
largest_collatz_num = 2
collatz_nums = []

for num in range (1, 1000000):
    n = num
    count = 1
    while n > 1 and num not in collatz_nums:
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = (n * 3) + 1
                count += 1

    if count > largest_seq:
        largest_seq = count
        largest_collatz_num = num
        collatz_nums.insert(0, largest_collatz_num)

print(f'Num: {largest_collatz_num}, Count: {largest_seq}')
print(f'Clocked in at {time.time()-start} second(s)')
print(f'Collatz_nums: {collatz_nums}')
