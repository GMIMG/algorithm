from collections import deque


N, K = map(int, input().split())


def bfs():
    q = deque()
    q.append((N, 0))
    visit = set()
    while q:
        now, time = q.popleft()
        if now == K:
            return time
        if now in visit or now < 1:
            continue
        visit.add(now)
        q.append((now - 1, time + 1))
        if now < K:
            q.append((now + 1, time + 1))
            q.append((now * 2, time + 1))


t = bfs()
print(t)