a = 1
for i in range(1,int(input())+1):
    a *= i
i = 10
while a % i ==0:
    i *= 10
print(len(str(i))-2)