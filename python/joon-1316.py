import sys
input=sys.stdin.readline
a=int(input())
n=0
for i in range(a):
    b=[0]*123
    c=str(input())
    for j in range(len(c)):
        if b[ord(c[j])]!=0 and c[j-1] !=c[j]:
            n+=1
            break
        else:
            b[ord(c[j])]=1
print(a-n)