from collections import deque


def bfs(q):
    now = 0
    visit = set()
    while q:
        nr, nc = q.popleft()
        if (nr,nc) in visit:
            continue
        visit.add((nr,nc))
        now += 1
        for i in range(4):
            next_r = nr + dr[i]
            next_c = nc + dc[i]
            if next_r < 0 or next_c < 0 or next_r >= N or next_c >= M:
                continue
            if not board[next_r][next_c]:
                q.append((next_r, next_c))
    return now


N, M = map(int, input().split())
dr = (-1,1,0,0)
dc = (0,0,-1,1)
result = [[0]*M for _ in range(N)]

board = []
for r in range(N):
    board.append([int(c) for c in input()])

for r in range(N):
    for c in range(M):
        if board[r][c]:
            result[r][c] = bfs(deque([(r,c)]))

for r in result:
    print(*r, sep = '')
