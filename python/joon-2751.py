import sys
input = sys.stdin.readline
n = int(input())
b = []
for i in range(n):
    b.append(int(input()))
b.sort()
for i in range(n):
    print(b[i]) #pop제거