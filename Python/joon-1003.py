def p(a,i,j,b):
    if i>j:
        print(b,a)
        return a
    else:
        i+=1
        a,b=a+b,a
        p(a,i,j,b)

n = int(input())
for i in range(n):
    a=int(input())
    j=a
    if a == 0:print(1,0)
    else:p(0,1,j,1)