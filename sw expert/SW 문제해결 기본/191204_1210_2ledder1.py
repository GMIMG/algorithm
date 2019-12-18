for i in range(10):
    T = int(input())
    lst = []
    for r in range(100):
        lst.append(list(map(int, input().split())))
    nr = 99
    nc = lst[99].index(2)
    while True:
        nr = nr - 1
        flag = 0
        while (nc - 1 >= 0) and (lst[nr][nc - 1] == 1):
            nc = nc - 1
            flag = 1
        while (nc + 1 <= 99) and (lst[nr][nc + 1] == 1) and flag == 0:
            nc = nc + 1

        if nr == 0:
            break
        print((nr, nc))
    print('#{}'.format(T), nc)