t=int(input())
a = [25, 10, 5, 1]
for i in range(t):
    m=int(input())
    for j in a:
        print(m//j,end=' ')
        m %= j
    print()