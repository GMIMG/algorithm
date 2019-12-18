inp = input()
inp_st = inp.split()
N = int(inp_st[0])
M = int(inp_st[1])

MAX = M
visit = [0] * 10
lst = [0] * 10
# visit = [0 for i in range(100)]


def dfs(now, depth):
    if depth == MAX:
        for i in range(MAX):
            print(lst[i], end=' ')
        print()
        return 1

    for j in range(now+1, N+1):
        if visit[j] == 1:
            continue
        visit[j] = 1
        lst[depth] = j
        dfs(j, depth+1)
        visit[j] = 0
    return 0


dfs(0, 0)
