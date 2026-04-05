for i in range(int(input())):
    h, w, n = map(int, input().split())
    ww = (n-1) // h+1+100
    if ww-100 > w:
        ww-=1
    if n%h == 0:
        nn = h
    else:
        nn = n % h
    print(f"{nn}{str(ww)[1:]}")