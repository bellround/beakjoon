while 1:
    a = input()
    if a == '0':
        break
    print('yes') if a == a[::-1] else print('no')