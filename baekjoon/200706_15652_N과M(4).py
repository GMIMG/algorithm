def dfs(N, M, now, depth):
    if depth == M:
        print(*now)
        return 1
    s = now[-1] if now else 1
    for i in range(s, N + 1):
        dfs(N, M, now + [i], depth + 1)

N, M = map(int, input().split())
dfs(N, M, [], 0)