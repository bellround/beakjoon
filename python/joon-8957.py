n = int(input())
for i in range(n):
    a = 0
    b = str(input())
    s = 0
    for j in range(len(b)):
        if b[j] == 'O':
            s += 1
            a += s
        else:
            s = 0
    print(a)