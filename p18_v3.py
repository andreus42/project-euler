"""
# _____________________
# https://projecteuler.net/problem=18
# 9-10-2018, Monday, 22:01 - _____
"""

import time
start = time.time()

"""Start Here"""

r1 = [75]
r2 = [95, 64]
r3 = [17, 47, 82]
r4 = [18, 35, 87, 10]
r5 = [20, 4, 82, 47, 65]
r6 = [19, 1, 23, 75, 3, 34]
r7 = [88, 2, 77, 73, 7, 63, 67]
r8 = [99, 65, 4, 28, 6, 16, 70, 92]
r9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
r10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
r11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
r12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
r13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
r14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
r15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

highest_total = 0
for a in range(0,1):
    for b in range(a, a + 2):
        for c in range(b, b + 2):
            for d in range(c, c + 2):
                for e in range(d, d + 2):
                    for f in range(e, e + 2):
                        for g in range(f, f + 2):
                            for h in range(g, g + 2):
                                for i in range(h, h + 2):
                                    for j in range(i, i + 2):
                                        for k in range(j, j + 2):
                                            for l in range(k, k + 2):
                                                for m in range(l, l + 2):
                                                    for n in range(m, m + 2):
                                                        for o in range(n, n + 2):
                                                            for p in range(o, o + 2):
                                                                total = r1[a] + r2[b] + r3[c] + r4[d] + r5[e] + r6[f] + r7[g] + r8[h] + r9[i] + r10[j] + r11[k] + r12[l] + r13[m] + r14[n] + r15[o]
                                                                if total > highest_total:
                                                                    highest_total = total
                                                                total = 0

                                                                # print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)

print(highest_total)
print(f'Clocked in at {time.time()-start} second(s)')
