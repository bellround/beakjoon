def p(a,i,j,b):
    if i>=j:
        print(b)
        return a
    else:
        i+=1
        a,b=a+b,a
        p(a,i,j,b)

a=int(input())
j=a
if a == 0:print(0)
else:p(1,1,j,1)