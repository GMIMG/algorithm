import sys

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

mx = 0
mm = []

def dfs(now, money):
    if now >= N:
        mm.append(money)
        return
    next = now + lst[now][0]
    money += lst[now][1]

    for i in range(next, N+1):
        dfs(i, money)

for i in range(N):
    dfs(i, 0)
print(max(mm))