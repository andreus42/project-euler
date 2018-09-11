Row1 = list(map(int[75]))
Row2 = list(map(int[95, 64]))
Row1 = list(map(int[17, 47, 82]))
Row3 = list(map(int[18, 35, 87, 10]))
Row4 = list(map(int[20, 4, 82, 47, 65]))
Row5 = list(map(int[19, 1, 23, 75, 3, 34]))
Row6 = list(map(int[88, 2, 77, 73, 7, 63, 67]))
Row7 = list(map(int[99, 65, 4, 28, 6, 16, 70, 92]))
Row8 = list(map(int[41, 41, 26, 56, 83, 40, 80, 70, 33]))
Row9 = list(map(int[41, 48, 72, 33, 47, 32, 37, 16, 94, 29]))
Row10 = list(map(int[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]))
Row11 = list(map(int[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]))
Row12 = list(map(int[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]))
Row13 = list(map(int[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]))
Row14 = list(map(int[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]))

for each1 in Row1:
    print("row1")
    for each2 in Row2:
        print("row2")
        for each3 in Row3:
            print("row3")
            for each4 in Row4:
                print("row4")
                for each5 in Row5:
                    print("row5")
                    for each6 in Row6:
                        print("row6")
                        for each7 in Row7:
                            print("row7")
                            for each8 in Row8:
                                print("row8")
                                for each9 in Row9:
                                    print("row9")
                                    for each10 in Row10:
                                        print("row10")
                                        for each11 in Row11:
                                            print("row11")
                                            for each12 in Row13:
                                                print("row12")
                                                for each13 in Row13:
                                                    print("row13")
                                                    for each14 in Row14:
                                                        print("row14")
                                                        for each15 in Row15:
                                                            print("row15")
                                                            total = each1+each2+each3+each4+each5+each6+each7+each8+each9+each10+each11+each12+each13+each14+each15
                                                            if total > highest_total:
                                                                highest_total = total
                                                            count += 1
                                                            print(f'total: {total}, count: {count}')
