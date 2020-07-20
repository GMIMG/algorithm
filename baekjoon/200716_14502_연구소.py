from collections import deque
import copy


def check_safe(board):
    safe = 0
    for r in board:
        for c in r:
            if not c:
                safe += 1
    return safe


def expose(board): # bfs
    q = deque()
    temp = copy.deepcopy(board)
    for idx_r, r in enumerate(temp):
        for idx_c, c in enumerate(r):
            if c == 2:
                q.append((idx_r,idx_c))
    while q:
        nr, nc = q.popleft()
        if temp[nr][nc] == 1:
            continue
        temp[nr][nc] = 2
        for i in range(4):
            next_r = nr + dr[i]
            next_c = nc+dc[i]
            if next_r < 0 or next_c < 0 or next_r >= N or next_c >= M:
                continue
            if temp[next_r][next_c] == 2:
                continue
            q.append((next_r,next_c))
    return check_safe(temp)




def set_wall(nr,nc,depth, board): # dfs
    if depth == 3:
        # for i in range(N):
        #     print(board[i])
        # print()
        result.append(expose(board))
        return
    for r in range(nr,N):
        for c in range(M):
            if nr == r and c < nc:
                continue

            if not board[r][c]:
                board[r][c] = 1
                set_wall(r,c,depth+1, board)
                board[r][c] = 0



N, M = map(int, input().split())
board = [list(map(int,input().split())) for i in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = []
for r in range(N):
    for c in range(M):
        if not board[r][c]:
            board[r][c] = 1
            set_wall(r,c,1, board)
            board[r][c] = 0

print(max(result))
