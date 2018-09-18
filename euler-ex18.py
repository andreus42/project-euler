import time
start = time.time()

node = [[int(num) for num in line.split(' ')] for line in open('018.txt').readlines()]

print(node)

for i in range(13, -1, -1):
    for j in range(i+1):
        node[i][j] += max(node[i+1][j], node[i+1][j+1])
        # print(node[i][j])
        # print(i,j)

print(node[0][0])

print(node)

print(f'Clocked in at {time.time()-start} second(s)')
