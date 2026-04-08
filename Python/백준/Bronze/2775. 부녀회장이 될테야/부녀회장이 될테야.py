n = int(input())
a = [[1] * 20 for i in range(20)]
for i in range(1,20):
    for j in range(1, 20):
        a[i][j] = a[i-1][j] + a[i][j-1]

for i in range(n):
    x = int(input())
    y = int(input())
    print(a[x+1][y-1])