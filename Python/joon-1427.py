a = [0] * 10
moon = str(input())
for i in range(len(moon)):
    a[int(moon[i])] += 1
for i in range(9,-1,-1):
    print(str(i) * a[i],end='')