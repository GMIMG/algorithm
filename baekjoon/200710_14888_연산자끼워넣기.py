import sys

N = int(sys.stdin.readline())
num = tuple(map(int, input().split()))
operator = list(map(int, input().split()))
op = ['+', '-', '*', '//']
result = []

def dfs(now, i, operator, sol):
    # print(now, i, operator, sol)

    if i == 0:
        sol += num[now]
    elif i == 1:
        sol -= num[now]
    elif i == 2:
        sol *= num[now]
    elif i == 3:
        if sol < 0:
            sol = -1*((-1*sol)//num[now])
        else:
            sol //= num[now]

    if now == N-1:
        result.append(sol)
        return

    for i in range(4):
        if not operator[i]:
            continue
        operator[i] -= 1
        dfs(now+1, i, operator, sol)
        operator[i] += 1


dfs(0, 0, operator, 0)

print(max(result))
print(min(result))