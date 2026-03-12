group=['','D0','D+','C0','C+','B0','B+','A0','A+']
n=0
m=0
for i in range(20):
    a, b, c = map(str, input().split())
    if c in group:
        n += float(b) * ((group.index(c)+1) / 2)
        m += float(b)
print(n // m)