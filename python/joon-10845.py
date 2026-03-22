import sys
input = sys.stdin.readline #시간 초과 해결을 위해 입력을 효율적으로 바꿈
a = []
for i in range(int(input())):
    b = list(map(str, input().split()))
    if b[0] == 'push':
        a.append(b[1])
    elif b[0] == 'pop':
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop(0))
    elif b[0] == 'size':
        print(len(a))
    elif b[0] == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif b[0] == 'front':
        if len(a) == 0:
            print(-1)
        else:
            print(a[0])
    else:
        if len(a) == 0:
            print(-1)
        else:
            print(a[len(a)-1])