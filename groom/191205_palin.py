def ispal(r, c, N, mat):
    # 홀짝 판단
    if N % 2:
        odd = 1
    else:
        odd = 0

    check = 1
    for i in range(N//2):
        if mat[r][c + i] != mat[r][c + N - 1 - i]:
            check = 0
    #if check:
    #    print(r,c,mat[r][c:c+N])
    return check





def ispal2(r, c, N, mat):
    # 홀짝 판단
    if N % 2:
        odd = 1
    else:
        odd = 0

    check = 1
    for i in range(N//2):
        if mat[r + i][c] != mat[r + N - 1 - i][c]:
            check = 0
    #if check:
    #    print(r,c,[mat[_][c] for _ in range(r, r+N)])
    return check






T = 0
for t in range(10):
    T = T + 1
    N = int(input())

    # input
    mat = list()

    for _ in range(8):
        ROW = input()
        row = list(ROW)
        mat.append(row)


    sum = 0
    visit = dict()
    for r in range(8):
        for c in range(0, 8 - N + 1):
            if ispal(r, c, N, mat):
                visit[''.join(mat[r][c:c + N])] = True
                sum = sum + 1

    for c in range(8):
        for r in range(0, 8 - N + 1):
            if ispal2(r, c, N, mat):
                visit[''.join([mat[_][c] for _ in range(r, r + N)])] = True
                sum = sum + 1
    #print('#{}'.format(T), len(visit))
    print('#{}'.format(T), sum)
