from collections import deque


def bfs(q, num):
    now = 0
    while q:
        nr, nc = q.popleft()
        if visit[nr][nc]:
            continue
        visit[nr][nc] = 1
        area[nr][nc] = num
        now += 1
        for i in range(4):
            next_r = nr + dr[i]
            next_c = nc + dc[i]
            if next_r < 0 or next_c < 0 or next_r >= N or next_c >= M:
                continue
            if not board[next_r][next_c]:
                q.append((next_r, next_c))
    area_sum[num] = now


N, M = map(int, input().split())
dr = (-1,1,0,0)
dc = (0,0,-1,1)
area = [[0]*M for _ in range(N)]
area_sum = {}
result = [[0]*M for _ in range(N)]
visit = [[0]*M for _ in range(N)]
board = []

for r in range(N):
    board.append([int(c) for c in input()])
area_num = 0
for r in range(N):
    for c in range(M):
        if not board[r][c] and not visit[r][c]:
            area_num += 1
            bfs(deque([(r,c)]), area_num)

# print(area)

for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            visit_area = set()
            for i in range(4):
                next_r = r + dr[i]
                next_c = c + dc[i]
                if next_r < 0 or next_c < 0 or next_r >= N or next_c >= M:
                    continue
                if area[next_r][next_c]:
                    visit_area.add(area[next_r][next_c])

            result[r][c] = 1
            for va in visit_area:
                result[r][c] += area_sum[va]
            result[r][c] %= 10

for r in result:
    print(*r, sep = '')
