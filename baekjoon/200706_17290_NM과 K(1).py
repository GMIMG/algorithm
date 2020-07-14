N, M, K = map(int, input().split())
m = [list(map(int, input().split())) for i in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def neighbor(r,c,res):
    for re in res:
        for i in range(4):
            if (r == (re[0] + dr[i])) and (c == (re[1] + dc[i])):
                return True
    return False


def dfs(nr,nc,depth, now, mx, res):
    if nr < 0 or nc < 0 or nr >= N or nc >= M:
        return 0
    if depth == K:
        if not mx:
            return now
        return max(now, mx)
    res += [(nr, nc)]
    for r in range(nr, N):
        for c in range(M):
            if neighbor(r,c, res):
                continue
            if r == nr and c <= nc:
                continue
            # print(nr, nc, r, c, mx, now, res)
            mx = dfs(r,c,depth+1, now+m[r][c], mx, res)
    return mx

mm = 0
for i in range(N):
    for j in range(M):
        sol = dfs(i, j, 1, m[i][j], None, [])
        if sol:
            mm = max(mm, sol)

print(mm)