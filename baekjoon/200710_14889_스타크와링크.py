import sys


N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
result = []


def sum_skill(ateam):
    skill = 0
    for i in ateam:
        for j in ateam:
            skill += board[i][j]

    bteam = {i for i in range(N)} - set(ateam)
    for i in bteam:
        for j in bteam:
            skill -= board[i][j]
    return abs(skill)


def dfs(now, ateam, people):
    if people*2 == N:
        result.append(sum_skill(ateam))
        return

    for i in range(now+1, N):
        dfs(i, ateam + [i], people+1)


for i in range(N):
    dfs(i,[i],1)

print(min(result))