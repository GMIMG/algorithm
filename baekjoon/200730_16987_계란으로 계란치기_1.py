def dfs(depth, eggs_str):
    temp = 0
    for strength in eggs_str:
        if strength <= 0:
            temp += 1
    if temp == N-1:
        result.add(temp)
        return

    if depth == N-1 and eggs_str[depth] < 0:
        temp = 0
        for strength in eggs_str:
            if strength <= 0:
                temp += 1
        result.add(temp)
        return

    elif depth == N:
        temp = 0
        for strength in eggs_str:
            if strength <= 0:
                temp += 1
        result.add(temp)
        return

    if eggs_str[depth] > 0:
        for i in range(N):
            if depth != i and eggs_str[i] > 0:
                eggs_str[depth] -= eggs[i][1]
                eggs_str[i] -= eggs[depth][1]
                dfs(depth + 1, eggs_str)
                eggs_str[depth] += eggs[i][1]
                eggs_str[i] += eggs[depth][1]
    else:
        dfs(depth + 1, eggs_str)
    return


N = int(input())
eggs = [tuple(map(int, input().split())) for _ in range(N)]
eggs_str = []
for strength, weight in eggs:
    eggs_str.append(strength)

result = set()
dfs(0, eggs_str)

print(max(result))