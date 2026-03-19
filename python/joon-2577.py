a=int(input())
b=int(input())
c=int(input())
n = a * b * c
n=str(n)
for i in range(10):
    m=0
    for j in range(len(n)):
        if n[j] == str(i):
            m+=1
    print(m)