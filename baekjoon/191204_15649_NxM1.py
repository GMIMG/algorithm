inp = input()
[N, M] = map(int, inp.split())
visit = {}
lst = [0] * 10


def dfs(now, depth):
    # 탈출조건
    if depth == M:
        # 출력
        for i in range(M):
            print(lst[i], end=' ')
        print()
        return 1
    # 
    for j in range(1, N+1):
        if j in visit and visit[j]:
            continue
        visit[j] = True
        lst[depth] = j
        dfs(j, depth+1)
        visit[j] = False
    return 0


dfs(0, 0)
