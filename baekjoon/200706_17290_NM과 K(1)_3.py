is_first = True
ans = 0
board = []

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

board = sum(board, [])
visit = 0

def check(pivot, visit):
    if pivot < 1:
        return True
    elif not (pivot%M) and not visit&(1<<(pivot-M)):
        return True
    elif pivot < M and not visit & (1 << (pivot - 1)):
        return True
    elif pivot >= M and not visit&(1<<(pivot-1))\
    and not visit&(1<<(pivot-M)):
        return True
    return False

def dfs(tmp_sum, now, lvl, visit):
    # print(tmp_sum, now, lvl)
    if lvl == K:
        global ans, is_first
        if is_first:
            ans = tmp_sum
            is_first = False
        else:
            ans = max(ans,tmp_sum)
        return
    s = 0 if not lvl else now+1
    for i in range(s, N*M):
        if not check(i, visit):
            continue
        visit |= 1<<i
        dfs(tmp_sum+board[i], i, lvl+1, visit)
        visit = (visit & ~(1<<i))

dfs(0, 0, 0, 0)

# for i in range(N*M):
#     visit[i] = 1
#     dfs(board[i], i, 1)
#     visit[i] = 0

print(ans)