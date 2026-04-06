a = list(map(int, input().split()))
b = 0
for i in range(1, len(a)):
    if a[i] - a[i-1] == -1:
        b += 1
    elif a[i] - a[i - 1] == 1:
        b -= 1
if b == -7:
    print('ascending')
elif b == 7:
    print('descending')
else:
    print('mixed')