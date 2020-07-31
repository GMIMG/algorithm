def dfs(nr,nc,npos):
    global result

    if nr >= N or nc >= N:
        return 0
    if board[nr][nc] == 1:
        return 0
    elif npos == 2 and (board[nr][nc] or board[nr][nc-1] or board[nr-1][nc]):
        return 0
    if check[nr][nc][npos] != -1:
        return check[nr][nc][npos]
    if nr == N-1 and nc == N-1:
        return 1

    check[nr][nc][npos] = 0

    if npos == 0:
        check[nr][nc][npos] += dfs(nr, nc + 1, 0)
        check[nr][nc][npos] += dfs(nr + 1, nc + 1, 2)
    elif npos == 1:
        check[nr][nc][npos] += dfs(nr + 1, nc, 1)
        check[nr][nc][npos] += dfs(nr + 1, nc + 1, 2)
    elif npos == 2:
        check[nr][nc][npos] += dfs(nr, nc + 1, 0)
        check[nr][nc][npos] += dfs(nr + 1, nc, 1)
        check[nr][nc][npos] += dfs(nr + 1, nc + 1, 2)
    return check[nr][nc][npos]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[[-1]*3 for c in range(N)] for r in range(N)]

print(dfs(0,1,0))
