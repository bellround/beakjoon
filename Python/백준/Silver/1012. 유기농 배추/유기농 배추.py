import sys

sys.setrecursionlimit(1000000)

xx = [1, -1, 0, 0]
yy = [0, 0, 1, -1]

def dfs(x, y):
    if x >= n or y >= m or x < 0 or y < 0 or a[x][y] == 0:
        return
    a[x][y] = 0
    for i in range(4):
        dfs(x + xx[i], y + yy[i])

for ii in range(int(input())):
    m, n, k = map(int, input().split())
    a = [[0] * m for i in range(n)]
    for j in range(k):
        b, c = map(int, input().split())
        a[c][b] = 1
        
    tt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                dfs(i, j)
                tt += 1
    print(tt)