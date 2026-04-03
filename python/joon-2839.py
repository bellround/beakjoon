# 기초적인 다이내믹 프로그래밍 문제
import sys
sys.setrecursionlimit(100000)
def min_kg(kg, i):
    if kg < 0:
        return 0
    if memo[kg] <= i:
        return 0
    memo[kg] = min(i, memo[kg])
    min_kg(kg-5, i+1)
    min_kg(kg-3, i+1)
    return 0

kg = int(input())
memo = [100000] * (kg+1)
min_kg(kg,0)
if memo[0] != 100000:
    print(memo[0])
else:
    print(-1)