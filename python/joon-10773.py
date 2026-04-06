a = []
for i in range(int(input())):
    b = int(input())
    if b == 0:
        a.pop()
    else:
        a.append(b)
n = 0
for i in a:
    n += i
print(n)