(N, M) = map(int, input().split())
visit = dict()
lst = [0] * 10


def dfs(depth, now):
    if depth == M:
        for i in range(M):
            print(lst[i], end = ' ')
        print()
        return 1
    for v in range(now, N+1):
        if v == 0:
            continue
        if v in visit and visit[v]:
            continue
        visit[v] = True
        lst[depth] = v
        dfs(depth+1, v)
        visit[v] = False
    return 0


dfs(0, 0)
