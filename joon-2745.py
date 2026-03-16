a=['0','1','2','3','4','5','6','7','8','9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n,b=map(str,input().split())
b=int(b)
m, i ,j= 0, 0, len(n)-1
while j>=0:
    m += a.index(str(n[i])) * b ** j
    i+=1
    j-=1
print(m)