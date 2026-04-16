# 제귀제한 늘리기
import sys
sys.setrecursionlimit(100000)

# dfs로 정상배열 확인
def ndfs(x, y, st):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return 0
    if a[x][y] == st:
        a[x][y] = 'q'
        ndfs(x-1, y, st)
        ndfs(x+1, y, st)
        ndfs(x, y-1, st)
        ndfs(x, y+1, st)
        return 1
    return 0

# dfs로 다른 배열확인
def rdfs(x, y, st):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return 0
    if aa[x][y] == st:
        aa[x][y] = 'q'
        rdfs(x-1, y, st)
        rdfs(x+1, y, st)
        rdfs(x, y-1, st)
        rdfs(x, y+1, st)
        return 1
    return 0

n = int(input())
a = [[] for i in range(n)]
aa = [[] for i in range(n)]
rgb, nor=0, 0
# n*n 크기의 문자열로 된 배열생성 
for i in range(n):
    b = str(input())
    for j in range(n):
        a[i].append(b[j]) 
        if b[j] == 'G':
            aa[i].append('R')
        else:aa[i].append(b[j])
            
# 배열의 구역개수 입력  
for i in range(n):
    for j in range(n):
        if a[i][j] != 'q':
            if ndfs(i, j, a[i][j]) == True:
                nor += 1
        if aa[i][j] !='q':
            if rdfs(i, j, aa[i][j]) == True:
                rgb += 1
                
print(nor,rgb)