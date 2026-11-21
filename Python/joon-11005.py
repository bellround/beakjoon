a=['0','1','2','3','4','5','6','7','8','9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n, b=map(int,input().split())
m = []
while n > 0:
    m.append(a[n % b])
    n = n // b
for i in range(len(m)-1,-1,-1):
    print(m[i],end='')