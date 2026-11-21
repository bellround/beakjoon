a = []
m = 0
for i in range(8):
    a.append(input())
for i in range(8):
    for j in range(i % 2, 8, 2):
        if a[i][j] == "F":
            m += 1
print(m)