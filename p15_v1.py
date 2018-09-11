"""# Lattice paths
# https://projecteuler.net/problem=15
# 9-8-2018, 2:00pm-2:42pm

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Used this math approach:
https://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/

"""
# Timing Tools
# import time
# start = time.time()

"""
Answer:
answer = (math.factorial(40)/math.factorial(20)/math.factorial(20)
"""

# Make Matrix of width x height
width, height = 2, 2
Matrix = [[2 for x in range(width+1)] for y in range(height+1)]

# Traverse bottom row and set to 1 for 1 path option
for x in range(0, width):
    Matrix[height][x] = 1

# Traverse right column and set to 1 for 1 path option
for y in range(0, height):
    Matrix[y][width] = 1

# Set bottom corner to 0
Matrix[height][width] = 0

print(Matrix)


# print(f'Clocked in at {time.time()-start} second(s)')
