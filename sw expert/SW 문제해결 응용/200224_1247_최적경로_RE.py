def dfs(visit, now, now_dist, depth, solution):
    if depth == N:
        solution = min(solution, now_dist + dist_arr[now][1])
        return solution

    for i in range(1, N+2):
        if (visit & (1<<i)): continue
        visit |= (1<<i)
        next_dist = now_dist + dist_arr[now][i]
        solution = dfs(visit, i, next_dist, depth+1, solution)
        visit &= ~(1<<i)
    return solution

for T in range(int(input())):
    N = int(input())
    input_lst = list(map(int, input().split()))

    dist = []
    for _ in range(N+2):
        tmp = input_lst.pop(0)
        dist.append((tmp, input_lst.pop(0)))
    dist_arr = list()
    for r in range(N+2):
        temp_arr = []
        for c in range(N+2):
            temp_arr.append(abs(dist[r][0] - dist[c][0]) + abs(dist[r][1] - dist[c][1]))
        dist_arr.append(temp_arr)

    solution = 99999
    solution = dfs(1, 0, 0, 0, solution)
    print(f'#{T + 1}', solution)

