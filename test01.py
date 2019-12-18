inp = input()
inp_st = inp.split()
N = int(inp_st[0])
M = int(inp_st[1])

MAX = M
visit = [0] * 10
# visit = [0 for i in range(100)]


def dfs(now, depth):
    #if now == MAX + 1:
    #    return 1
    if depth == MAX:
        print(lst)
        return 1
    lst.append(now)
    for j in range(now+1, N+1):
    #for j in (1, N+1):
        if visit[j] == 1:
            continue
        visit[j] = 1
        dfs(j, depth+1)
        visit[j] = 0
    return 0


lst = []
for i in range(1, N+1):
    lst.append(i)
    visit[i] = 1
    dfs(i, 1)
    lst = []
    visit = [0] * 10
    # print()
