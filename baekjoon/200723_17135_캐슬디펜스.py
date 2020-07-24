from collections import deque
from itertools import combinations
from copy import deepcopy

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

max_turn = 0
for idx, r in enumerate(board):
    if r != [0,0,0,0,0]:
        max_turn = N - idx
        break

dr = (0,-1,0,1)
dc = (-1,0,1,0)

def sol(arrow_col):
    all_attack = 0
    for i in range(max_turn):
        all_attack += bfs(arrow_col, i)
    # print(all_attack)
    return all_attack


def bfs(arrow_col, now_turn):
    # print(f'{now_turn} start')
    q = deque()
    arrow_check = [0]*3
    attack = set()
    visit = set()

    for idx, col in enumerate(arrow_col):
        q.append((N-1-now_turn, col, idx, 1))
    # print(q)
    while q:
        nr, nc, arrow_idx, dd = q.popleft()
        # 방문한곳 체크
        if (nr, nc, arrow_idx) in visit:
            continue
        visit.add((nr,nc,arrow_idx))
        # 이미 공격한경우
        if arrow_check[arrow_idx]:
            continue
        # 사정거리보다 멀때
        if dd > D:
            continue
        # 적이 있으면
        if now_board[nr][nc] == 1:
            arrow_check[arrow_idx] = 1
            attack.add((nr,nc))
            continue
        for i in range(3):
            next_r = nr+dr[i]
            next_c = nc+dc[i]
            if next_r < 0 or next_c < 0 or next_r >= N or next_c >= M:
                continue
            q.append((next_r,next_c,arrow_idx,dd+1))
    for r, c in attack:
        now_board[r][c] = 0
    # print(attack)
    return len(attack)


mx_attack = 0
for arrow_col in combinations(range(M), 3):
    now_board = deepcopy(board)
    mx_attack = max(mx_attack, sol(arrow_col))
print(mx_attack)


# def dfs(now, visit):
#     for i in range(now+1, N):
#         if visit & (1<<i):
#             continue