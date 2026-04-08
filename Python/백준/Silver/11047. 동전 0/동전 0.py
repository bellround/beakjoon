import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] * (n + 1)
for i in range(n):
    a[i] = int(input())
    
for i in range(len(a)-2, -1, -1):
    if m // a[i] > 0:
        a[-1] += m // a[i]
        m %= a[i]
print(a[-1])