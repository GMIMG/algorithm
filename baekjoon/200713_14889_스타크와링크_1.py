from itertools import combinations


N = int(input())
board = [list(map(int, input().split())) for i in range(N)]


def sum_skill(ateam):
    skill = 0
    for i in ateam:
        for j in ateam:
            skill += board[i][j]

    bteam = set(range(N)) - set(ateam)
    for i in bteam:
        for j in bteam:
            skill -= board[i][j]
    return abs(skill)


mn = 987654321
for i in combinations(range(N-1), N//2):
    mn = min(mn, sum_skill(set(i)))
print(mn)