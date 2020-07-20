from collections import deque


def bfs():
    q = deque([(coin[0][0],coin[0][1],coin[1][0],coin[1][1],0)])
    visit = set()
    while q:
        r1,c1,r2,c2,t = q.popleft()
        if (r1,c1,r2,c2) in visit:
            continue
        if t >= 10:
            return -1
        visit.add((r1,c1,r2,c2))
        for i in range(4):
            check = 2
            nr1, nc1, check = new_coord(r1, c1, dr[i], dc[i], check)
            nr2, nc2, check = new_coord(r2, c2, dr[i], dc[i], check)
            if check == 1:
                return t + 1
            elif check == 0:
                continue
            if nr1 == nr2 and nc1 == nc2:
                continue
            q.append((nr1,nc1,nr2,nc2,t+1))
    return -1


def new_coord(r, c, dr, dc, check):
    nr, nc = r + dr, c + dc
    if nr < 0 or nc < 0 or nr >= N or nc >= M:
        check -= 1
    else:
        nr, nc = (r, c) if board[nr][nc] == 1 else (nr, nc)
    return nr, nc, check


N, M = map(int, input().split())
board = [[0]*M for _ in range(N)]
dr = (-1,1,0,0)
dc = (0,0,-1,1)


coin = []

for r in range(N):
    row = input()
    for c, col in enumerate(row):
        if col == 'o':
            coin.append((r,c))
        elif col == '#':
            board[r][c] = 1
print(bfs())


