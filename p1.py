# p1: Multiples of 3 and 5
# Sum all multiples of 3 and 5 below 1000
# 8-5-2018, 8:25am-8:49am (about ~15, with some interuptions)

sum = 0;

for n in range(1,1000):
    if (n%3==0) or (n%5==0):
        sum += n

print(sum)
