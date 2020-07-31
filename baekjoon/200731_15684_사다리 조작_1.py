from itertools import combinations


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
        if n == 1:
            return False

    temp = order.copy()
    for ladder in sorted(ladders, key= lambda x:x[0]):
        temp[ladder[1]-1], temp[ladder[1]] = temp[ladder[1]], temp[ladder[1]-1]
    if temp == order:
        return True
    else:
        return False


def check(ladders, a, b):
    for ladder in ladders:
        if (ladder[0] == a) and ((ladder[1] == b + 1) or (ladder[1] + 1 == b) or ((ladder[1]) == b)):
            return False
    return True


def check_able(ab, num_ladder):
    for i in range(num_ladder):
        for j in range(i+1, num_ladder):
            if ab[i][0] == ab[j][0] and ((ab[i][1] == ab[j][1] + 1) or (ab[i][1] + 1 == ab[j][1])):
                return False
    return True


def put_ladder(num_ladder):
    for ab in combinations(able, num_ladder):
        if not check_able(ab, num_ladder):
            continue
        ladders.extend(ab)
        # print(ladders)
        if change():
            return True
        else:
            for _ in range(num_ladder):
                ladders.pop()
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


able = []
for a in range(1, H+1):
    for b in range(1, N):
        if check(ladders, a, b):
            able.append((a,b))
print(sol())
