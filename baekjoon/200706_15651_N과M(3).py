def dfs(N, M, now, depth):
    if depth == M:
        print(*now)
        return 1
    for i in range(1, N + 1):
        dfs(N, M, now + [i], depth + 1)

N, M = map(int, input().split())
dfs(N, M, [], 0)