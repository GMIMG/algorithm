from copy import deepcopy


def hit(eggs_str, a, b):
    eggs_str[a] -= eggs[b][1]
    eggs_str[b] -= eggs[a][1]
    return eggs_str


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
                dfs(depth + 1, hit(deepcopy(eggs_str), depth, i))
        return
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