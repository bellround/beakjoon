import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
k = 0

def dfs(x, y):
    global k
    if x == m - 1 and y == n - 1:
        k = 1
        return
    a[y][x] = 0
    for dx, dy in ((1, 0), (0, 1)):
        nx, ny = x + dx, y + dy
        if nx < m and ny < n and a[ny][nx] == 1:
            dfs(nx, ny)


m, n = map(int, input().split()) 
a = [list(map(int, input().split())) for i in range(n)]

dfs(0, 0)
print("Yes" if k else "No")