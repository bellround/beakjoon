# 벌집문제
n = int(input())-1
i = 0
while n>0:
    i += 1
    n -= i*6
print(i+1)