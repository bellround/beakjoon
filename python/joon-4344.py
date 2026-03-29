for i in range(int(input())):
    n = list(map(int, input().split()))
    jum = 0
    num = 0
    for j in range(1,n[0]+1):
        jum += n[j]
    jum /= n[0]
    for j in range(1,n[0]+1):
        if (n[j] > jum):
            num += 1
    print(f'{round((num / n[0]) * 100,3)}%')