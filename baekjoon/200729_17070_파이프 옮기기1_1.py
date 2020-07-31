def dfs(nr,nc,npos,stack):
    global result

    if nr >= N or nc >= N:
        return
    if npos == 2 and (board[nr][nc] or board[nr][nc-1] or board[nr-1][nc]):
        return
    if check[nr][nc][npos]:
        result += 1
        return

    if nr == N-1 and nc == N-1:
        while stack:
            r,c,pos = stack.pop()
            check[r][c][pos] = 1
        result += 1
        return

    if npos == 0:
        dfs(nr, nc + 1, 0, stack+[(nr,nc + 1,npos)])
        dfs(nr + 1, nc + 1, 2, stack+[(nr+1,nc + 1,npos)])
    elif npos == 1:
        dfs(nr + 1, nc, 1, stack+[(nr+1,nc,npos)])
        dfs(nr + 1, nc + 1, 2, stack+[(nr+1,nc + 1,npos)])
    elif npos == 2:
        dfs(nr, nc + 1, 0, stack+[(nr,nc + 1,npos)])
        dfs(nr + 1, nc, 1, stack+[(nr+1,nc,npos)])
        dfs(nr + 1, nc + 1, 2, stack+[(nr+1,nc + 1,npos)])


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
success = set()
result = 0
check = [[[0]*3 for c in range(N)] for r in range(N)]

dfs(0,1,0,[])
print(result)
