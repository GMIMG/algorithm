from collections import deque


def dfs(q, now_energy):
    # print(q, now_energy)
    l = len(q)
    if l == 2:
        result.append(now_energy)
        return
    for i in range(1, l-1):
        next_energy = now_energy + q[i-1] * q[i+1]
        temp_value = q[i]
        del q[i]
        dfs(q, next_energy)
        q.insert(i, temp_value)


N = int(input())
lst = list(map(int, input().split()))
q = deque(lst)
result = []
dfs(q, 0)
print(max(result))