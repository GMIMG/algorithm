from collections import deque
# teleport = {i:i for i in range(101)}
teleport = {}
N, M = map(int, input().split())
for _ in range(N+M):
    key, value = map(int, input().split())
    teleport[key] = value
time = [100]*(100+1)


def bfs():
    q = deque([1])
    time[1] = 0
    while q:
        now = q.popleft()
        if now == 100:
            break
        for i in range(1, 7):
            if now+i > 100:
                continue
            next = teleport.get(now + i, now + i) # next = teleport[now+i]
            if time[next] < time[now] + 1:
                continue
            time[next] = time[now] + 1
            q.append(next)
bfs()
print(time[100])
