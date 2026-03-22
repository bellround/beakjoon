n = int(input())
a = 0
while n:
    if n%3 == 0:
        a +=1
        n //= 3
    elif n % 2 == 0:
        a += 1
        n //= 2
    else:
        a += 1
        n -= 1
print(a-1)