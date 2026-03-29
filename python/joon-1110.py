b = str(0) + str(input()) # 한자릿수일떄 방지
a = b # 복사
i = 0  # 몇번 반복했는지
while 1:
    i += 1
    a = str((int(a)%10 * 10))[0] + str(int(a[0])+int(a[1]))[-1] # 계산식
    if a == b: # 같으면 나가기
        break
print(i)