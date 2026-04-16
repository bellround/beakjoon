k=int(input())
a=list(map(int, input().split()))
g=[]
l=2**k-1
for i in range(0,k):
    g.append([])
    for j in range(2**i-1,l,2**(i+1)):
        g[i].append(a[j])
for i in range(k-1,-1,-1):
    for j in range(len(g[i])):
        print(g[i][j],end=' ')
    print()