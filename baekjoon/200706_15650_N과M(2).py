def dfs(N, M, checked, now, depth):
    if depth == M:
        print(*now)
        return 1
    s = now[-1] if now else 1
    for i in range(s, N + 1):
        # if now and i < now[-1]:
        #     continue
        if checked & (1 << i):
            continue
        dfs(N, M, checked | (1<<i), now + [i], depth + 1)

N, M = map(int, input().split())
checked = 0
dfs(N, M, checked, [], 0)