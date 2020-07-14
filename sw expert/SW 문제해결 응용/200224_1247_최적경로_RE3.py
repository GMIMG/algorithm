def dfs(visit, now, depth):
    # 마지막 노드라면 거리 리턴 시작
    if depth == N:
        return dist_arr[now][1]

    # 이미 방문했던 경로라면
    if visit in dp[now]:
        return dp[now][visit]

    solution = 99999
    for i in range(2, N + 2):
        if visit & (1 << i): continue
        # visit |= (1 << i)
        solution = min(solution, dfs(visit | (1 << i), i, depth + 1) + dist_arr[now][i])
        # visit &= ~(1 << i)
    # 지금 노드에서 최소값 저장
    dp[now][visit] = solution
    return solution


for T in range(1, 1 + int(input())):
    N = int(input())
    input_lst = list(map(int, input().split()))
    dist = [(input_lst[i*2], input_lst[i*2 + 1]) for i in range(N+2)]
    dist_arr = list()
    for r in range(N + 2):
        temp_arr = []
        for c in range(N + 2):
            temp_arr.append(abs(dist[r][0] - dist[c][0]) + abs(dist[r][1] - dist[c][1]))
        dist_arr.append(temp_arr)
    dp = [dict() for _ in range(N+2)]
    solution = dfs(1, 0, 0)
    print(f'#{T}', solution)