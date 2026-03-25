n = int(input())
a = list(map(int, input().split()))
t, p = map(int, input().split())
ts = 0
penM = n // p
penN = n - (n//p*p)
for i in a:
    if i % t != 0:
        ts +=1
    ts += i // t
print(ts)
print(penM,penN)