from collections import deque


def bfs(q):
    while q:
        nr, nc, now, depth = q.popleft()
        if depth == 5:
            result.add(now)
            continue
        for i in range(4):
            next_r = nr + dr[i]
            next_c = nc + dc[i]
            if next_r < 0 or next_r >= 5 or next_c < 0 or next_c >= 5:
                continue
            q.append((next_r,next_c,now*10+board[next_r][next_c], depth+1))


board = [list(map(int, input().split())) for _ in range(5)]
dr = (-1,1,0,0)
dc = (0,0,-1,1)
result = set()

for r in range(5):
    for c in range(5):
        bfs(deque([(r,c,board[r][c],0)]))
        # dfs(r,c,board[r][c],0)
print(len(result))




# def dfs(nr,nc,now,depth):
#     if depth == 5:
#         result.add(now)
#         return
#     for i in range(4):
#         next_r = nr + dr[i]
#         next_c = nc + dc[i]
#         if next_r < 0 or next_r >= 5 or next_c < 0 or next_c >= 5:
#             continue
#         dfs(next_r, next_c, now*10+board[next_r][next_c], depth+1)