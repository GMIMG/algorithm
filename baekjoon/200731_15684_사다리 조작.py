N, M, H = map(int, input().split())
ladders = [tuple(map(int,input().split())) for _ in range(M)]
MAX_LADDER = (N//2) * H

order = []
for i in range(1, N + 1):
    order.append(i)


def change():
    num = [0]*(N+1)
    for ladder in ladders:
        num[ladder[1]] += 1
    for n in num:
        if n%2 == 1:
            return False

    temp = order.copy()
    for i in range(1, H + 1):
        for ladder in ladders:
            if ladder[0] == i:
                temp[ladder[1]-1], temp[ladder[1]] = temp[ladder[1]], temp[ladder[1]-1]
    if temp == order:
        return True
    else:
        return False


def check(a, b):
    for ladder in ladders:
        if (ladder[0] == a) and ((ladder[1] == b + 1) or (ladder[1] + 1 == b) or ((ladder[1] + 1) == b + 1)):
            return False
    return True

def dfs(depth, oa, ob, num_ladder):
    # print(ladders)
    if depth == num_ladder:
        if change():
            return True
        else:
            return False

    for a in range(oa, H+1):
        for b in range(1, N):
            if a == oa and b <= ob:
                continue
            if check(a, b):
                ladders.append((a,b))
                if dfs(depth+1, a, b, num_ladder):
                    return True
                ladders.pop()
    return False


def put_ladder(num_ladder):
    if dfs(0, 1, 0, num_ladder):
        return num_ladder
    else:
        return -1


def sol():
    for i in range(MAX_LADDER - M + 1):
        if i > 3:
            return -1
        if (M + i) % 2 == 1:
            continue
        if put_ladder(i) != -1:
            return i
    return -1


print(sol())
