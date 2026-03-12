a=str(input())
kroa=['c=','c-','d-','lj','nj','s=','z=']
n = len(a)
for i in range(len(a)-1):
    for j in kroa:
        if a[i] == j[0] and a[i+1] == j[1]:
            n -= 1
            if j[0] == 'z' and a[i-1] == 'd':
                n -= 1        
print(n)