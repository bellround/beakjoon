import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    m = (a ** ( (b - 1) % 4 + 1 ))%10
    print(10 if m == 0 else m)