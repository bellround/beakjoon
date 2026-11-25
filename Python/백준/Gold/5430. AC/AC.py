import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
for i in range(n):
    s = input()
    m = int(input())
    temp = input()
    a = list(map(int, temp[1:-2].split(","))) if m > 0 else []
    a = deque(a)
    t = 0
    for i in s:
        if i == "R":
            t += 1
        elif i == "D":
            m -= 1
            if m < 0:
                break
            if t % 2 == 1:
                a.pop()
            else:
                a.popleft()
    if m < 0:
        print("error")
        continue
    elif m == 0:
        print("[]")
        continue
    print("[",end="")
    if t %2 == 1:
        for i in range(len(a) -1, 0, -1):
            print(a[i],end=",")
        print(f"{a[0]}]")
    else:
        for i in range(len(a) -1):
            print(a[i],end=",")
        print(f"{a[-1]}]")
    