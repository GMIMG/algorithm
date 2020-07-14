N, M, K = map(int, input().split())
m = [list(map(int, input().split())) for i in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

lst = [(m[r][c], r, c) for r in range(N) for c in range(M)]
sorted_lst = sorted(lst, key=lambda x:-x[0])

def neighbor(r,c,stack):
    for re in stack:
        for i in range(4):
            if (r == (sorted_lst[re][1] + dr[i])) and (c == (sorted_lst[re][2] + dc[i])):
                return True
    return False


def dfs(now, depth, stack, sum_value, mx):
    # print(depth, now, sum_value, stack)
    if depth == K:
        return sum_value

    for i in range(len(sorted_lst)):
        if i in stack:
            continue
        if stack and neighbor(sorted_lst[i][1], sorted_lst[i][2], stack):
            continue
        stack.append(i)
        sol = dfs(i, depth + 1, stack, sum_value + sorted_lst[i][0], mx)
        stack.pop()
        if sol:
            mx = max(sol, mx)
    return mx
print(dfs(-1, 0, [], 0, 0))