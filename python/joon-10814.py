n = int(input())
b = [[0] for i in range(300)]  #정렬 배렬
for i in range(n):
    a = list(map(str, input().split())) #입력받기
    b[int(a[0])][0] += 1  # 나이
    b[int(a[0])].append(a[1])  #가입순서
for i in range(len(b)):
    if b[i][0] == 0:  #없으면 패스
        pass
    else:  #있으면 그 나이 전부 출력
        for j in range(b[i][0]):
            print(i,b[i][j+1])