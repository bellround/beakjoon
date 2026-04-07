a = int(input())
memo = "0abcdefghijklmnopqrstuvwxyz"
b = str(input())
n = 0
for j in range(a-1,-1,-1):
    n += (memo.index(b[j]) % 27) * 31 ** j
print(n % 1234567891)