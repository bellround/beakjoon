# 소수찾기
n = int(input())
a =list(map(int, input().split()))
m = 0
for i in range(n):
    if a[i] == 0 or a[i] == 1:
        continue
    for j in range(2,a[i]):
        if a[i] % j == 0:
            a[i] = -1
            break
    if a[i] != -1:
        m+=1
print(m)