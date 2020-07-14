N, M, K = map(int, input().split())
m = [list(map(int, input().split())) for i in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


lst = [(m[r][c], r, c) for r in range(N) for c in range(M)]
sorted_lst = sorted(lst, key=lambda x:-x[0])

# print(sorted_lst)

def neighbor(r,c,stack):
    for re in stack:
        for i in range(4):
            if (r == (sorted_lst[re][1] + dr[i])) and (c == (sorted_lst[re][2] + dc[i])):
                return True
    return False

def dfs(now, depth, sum_value, mx, stack):
    # print(depth, now, mx, sum_value, stack)
    if stack and neighbor(sorted_lst[now][1], sorted_lst[now][2], stack):
        return sum_value
    if depth != 0:
        sum_value += sorted_lst[now][0]
    # print(now, depth, sum_value, restrict)

    if depth == K:
        return sum_value

    for i in range(len(sorted_lst)):
        if i in stack:
            continue
        stack.append(i)
        sol = dfs(i, depth + 1, sum_value, mx, stack)
        stack.pop()
        if mx:
            mx = max(mx, sol)
        else:
            mx = sol
    return mx

print(dfs(-1, 0, 0, None, []))