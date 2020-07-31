from collections import deque

def bfs():
    q = deque()
    q.append((0,1,0)) # (row,col,pos)
    result = 0
    visit = set()
    while q:
        nr, nc, npos = q.popleft()
        # print(nr,nc,npos)
        if nr == N-1 and nc == N-1:
            result+=1
            continue
        # if (nr,nc,npos) in visit:
        #     continue
        visit.add((nr,nc,npos))
        if npos == 0:
            if nc+1 < N and board[nr][nc+1] != 1:
                q.append((nr, nc+1, 0))
            if nc+1 < N and nr+1 < N \
                and board[nr+1][nc] != 1 \
                and board[nr][nc+1] != 1 \
                and board[nr+1][nc+1] != 1:
                q.append((nr+1, nc+1, 2))
        elif npos == 1:
            if nr+1 < N and board[nr+1][nc] != 1:
                q.append((nr+1, nc, 1))
            if nc+1 < N and nr+1 < N \
                and board[nr+1][nc] != 1 \
                and board[nr][nc+1] != 1 \
                and board[nr+1][nc+1] != 1:
                q.append((nr+1, nc+1, 2))
        else:
            if nc+1 < N and board[nr][nc+1] != 1:
                q.append((nr, nc+1, 0))
            if nr+1 < N and board[nr+1][nc] != 1:
                q.append((nr+1, nc, 1))
            if nc+1 < N and nr+1 < N \
                and board[nr+1][nc] != 1 \
                and board[nr][nc+1] != 1 \
                and board[nr+1][nc+1] != 1:
                q.append((nr+1, nc+1, 2))
    return result


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(bfs())
