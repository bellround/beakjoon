n = int(input())
b = []
for i in range(n):
    b.append(int(input()))
b.sort()
for i in range(n):
    print(b.pop(0))