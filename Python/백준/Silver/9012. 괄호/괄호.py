n = int(input())
for i in range(n):
    a=[0,0,0]
    b = str(input())
    for j in range(len(b)):
        if b[j] == '(':
            a[0] += 1
            a[1] -= 1
        elif b[j] == ')' and a[0] > 0:
            a[1] += 1
            a[0] -=1
        else:
            a[2] = 1
    if a[0] == a[1] and a[2] == 0:
        print('YES')
    else:
        print('NO')