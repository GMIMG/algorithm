def pal(r, c, N, mat):
    check = 1
    for i in range(N//2):
        if mat[r][c + i] != mat[r][c + N - 1 - i]:
            check = 0
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
    rev_mat = list(map(list, zip(*mat)))

    s = 0
    visit = dict()
    for r in range(8):
        for c in range(0, 8 - N + 1):
            if pal(r, c, N, mat):
                s = s + 1

    for r in range(8):
        for c in range(0, 8 - N + 1):
            if pal(r, c, N, rev_mat):
                s = s + 1
    print('#{}'.format(T), sum)
