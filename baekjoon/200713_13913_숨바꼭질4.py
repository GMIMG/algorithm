from collections import deque


N, K = map(int, input().split())


def bfs():
    q = deque()
    q.append(([K], 0))
    visit = set()
    while q:
        lst, time = q.popleft()
        now = lst[0]
        if now == N:
            return lst, time
        visit.add(now)

        if now + 1 not in visit:
            q.append(([now + 1] + lst, time + 1))
        if now > N:
            if now - 1 not in visit:
                q.append(([now - 1] + lst, time + 1))
            if not now % 2 and now // 2 not in visit:
                q.append(([now // 2] + lst, time + 1))

sol, t = bfs()
print(t)
print(*sol)