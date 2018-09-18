"""
# _____________________
# https://projecteuler.net/problem=18
# 9-10-2018, Monday, 22:01 - _____
"""

# Timing Tools
# import time
# start = time.time()

"""Start Here"""

Row1 = [3]
Row2 = [7, 4]
Row3 = [2, 4, 6]
Row4 = [8, 5, 9, 3]

#       [75]
#     [95, 64]
#   [17, 47, 82]
# [18, 35, 87, 10]

highest_total = 0
total = 0
count = 0
highest_seq = []
last_seq = []
n = 0
for each1 in range(n,n+2):
    print('Loop1')
    for each2 in range(each1,each1+2):
        print('Loop2')
        for each3 in range(each2,each2+2):
            print('Loop3')
            for each4 in range(each3,each3+2):
                print('Loop4')
                total += each1+each2+each3+each4
                seq = (Row1[n], Row2[each1], Row3[each2], Row4[each3])

                if total > highest_total:
                    highest_total = total
                    highest_seq = (Row1[n], Row2[each1], Row3[each2], Row4[each3])
                    last_seq = seq
                    highest_total = total

                    print(seq)
                    count += 1
                    print(f'count: {count}')
                    input()
                    total = 0

print(f'Total: {highest_total}, Sum count: {count}, highest_seq: {highest_seq}')

highest_total = 0
total = 0
count = 0
n = 0

# def best_path([a]):

# total += val
# count +=1
# if total > highest_total:
#     highest_total = total
# total = 0
# total_sum = sum(highest_seq)
# print(f'Total: {total_sum}, Sum count: {count}, highest_seq: {highest_seq}')


# print(f'Answer: {answer}')
# print(f'Clocked in at {time.time()-start} second(s)')
# recovery key 1355416-qVHrmCQcqcmNLeSHDkygw8oQKZ59aqYk0OIx2lxj
