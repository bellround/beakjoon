n=-1

def dfs(a,s,v):
    global n
    n+=1
    v[s]=1
    for i in a[s]:
        if v[i]==0:
            dfs(a,i,v)
            
gs=int(input())
ss=int(input())
a=[]
for i in range(gs+1):
    a.append([])
for i in range(ss):
    b=list(map(int,input().split()))
    a[b[0]].append(b[1])
    a[b[1]].append(b[0])
v=[0]*(gs+1)
dfs(a,1,v)
print(n)