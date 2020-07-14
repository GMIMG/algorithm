def p(selected):
    result = 0
    for i in selected:
        result += lst[i[0]][i[1]]
    ans.append(result)


def dfs(startr,visited, count):
    if count == K:
        p(selected)
        return

    for row in range(startr, N):
        for col in range(M):
            if not (row,col) in visited:
                selected.append((row,col))
                visited.append((row,col))
                for i in range(4):
                    if 0 <= row + dy[i] < N and 0 <= col + dx[i] < M:
                        visited.append((row+dy[i], col + dx[i]))
                dfs(row,visited, count + 1)
                selected.remove((row,col))
                visited.remove((row, col))
                for i in range(4):
                    if 0 <= row + dy[i] < N and 0 <= col + dx[i] < M:
                        visited.remove((row + dy[i], col + dx[i]))


N, M, K= map(int, input().split())
selected = []
visited = []
lst = []
ans = []
dy = [-1,0,1,0]
dx = [0,1,0,-1] # NESW
for row in range(N):
    lst.append(list(map(int, input().split())))
for row in range(N):
    for col in range(M):
        selected.append((row,col))
        visited.append((row, col))
        for i in range(4):
            if 0 <= row + dy[i] < N and 0 <= col + dx[i] < M:
                visited.append((row + dy[i], col + dx[i]))
        dfs(row,visited, 1)
        selected.remove((row,col))
        visited.remove((row, col))
        for i in range(4):
            if 0 <= row + dy[i] < N and 0 <= col + dx[i] < M:
                visited.remove((row + dy[i], col + dx[i]))
print(max(ans))

