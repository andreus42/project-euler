"""
# _____________________
# https://projecteuler.net/problem=18
# 9-10-2018, Monday, 22:01 - _____
"""

# Timing Tools
# import time
# start = time.time()

"""Start Here"""

Row1 = [75]
Row2 = [95, 64]
Row3 = [17, 47, 82]
Row4 = [18, 35, 87, 10]
Row5 = [20, 4, 82, 47, 65]
Row6 = [19, 1, 23, 75, 3, 34]
Row7 = [88, 2, 77, 73, 7, 63, 67]
Row8 = [99, 65, 4, 28, 6, 16, 70, 92]
Row9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
Row10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
Row11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
Row12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
Row13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
Row14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
Row15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

highest_total = 0
total = 0
count = 0

n = 0
for each1 in range(n,n+1):
    for each2 in range(each1,each1+2):
        for each3 in range(each2,each2+2):
            for each4 in range(each3,each3+2):
                for each5 in range(each4,each4+2):
                    for each6 in range(each5,each5+2):
                        for each7 in range(each6,each6+2):
                            for each8 in range(each7,each7+2):
                                for each9 in range(each8,each8+2):
                                    for each10 in range(each9,each9+2):
                                        for each11 in range(each10,each10+1):
                                            for each12 in range(each11,each11+2):
                                                for each13 in range(each12,each12+2):
                                                    for each14 in range(each13,each13+2):
                                                        for each15 in range(each14,each14+2):
                                                            total += each1+each2+each3+each4+each5+each6+each7+each8+each9+each10+each11+each12+each13+each14+each15
                                                            count +=1
                                                            if total > highest_total:
                                                                highest_total = total
                                                                highest_seq = (Row1[n], Row2[each1], Row3[each2], Row4[each3], Row5[each4], Row6[each5], Row7[each6], Row8[each7], Row9[each8], Row10[each9], Row11[each10], Row12[each11], Row13[each12], Row14[each13], Row15[each14])
                                                            total = 0
total_sum = sum(highest_seq)
print(f'Total: {total_sum}, Sum count: {count}, highest_seq: {highest_seq}')


# print(f'Answer: {answer}')
# print(f'Clocked in at {time.time()-start} second(s)')
# recovery key 1355416-qVHrmCQcqcmNLeSHDkygw8oQKZ59aqYk0OIx2lxj

# for each1 in Row1:
#     print("row1")
#     for each2 in Row2:
#         print("row2")
#         for each3 in Row3:
#             print("row3")
#             for each4 in Row4:
#                 print("row4")
#                 for each5 in Row5:
#                     print("row5")
#                     for each6 in Row6:
#                         print("row6")
#                         for each7 in Row7:
#                             print("row7")
#                             for each8 in Row8:
#                                 print("row8")
#                                 for each9 in Row9:
#                                     print("row9")
#                                     for each10 in Row10:
#                                         print("row10")
#                                         for each11 in Row11:
#                                             print("row11")
#                                             for each12 in Row13:
#                                                 print("row12")
#                                                 for each13 in Row13:
#                                                     print("row13")
#                                                     for each14 in Row14:
#                                                         print("row14")
#                                                         for each15 in Row15:
#                                                             print("row15")
#                                                             total = each1+each2+each3+each4+each5+each6+each7+each8+each9+each10+each11+each12+each13+each14+each15
#                                                             if total > highest_total:
#                                                                 highest_total = total
#                                                             count += 1
#                                                             print(f'total: {total}, count: {count}')
