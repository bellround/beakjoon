import sys
import heapq
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
INF=int(1e9)
n,m=map(int, input().split())
gr=[[] for i in range(n+1)]
guri=[INF]*(n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    gr[a].append((b, c))
    gr[b].append((a, c))

def dai(s):
    q=[]
    heapq.heappush(q,(0,s))
    while q:
        dist,now=heapq.heappop(q)
        if dist>guri[now]:
            continue
        for i in gr[now]:
            cost=dist+i[1]
            if cost<guri[i[0]]:
                guri[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return guri
dai(1)
print(guri[n])