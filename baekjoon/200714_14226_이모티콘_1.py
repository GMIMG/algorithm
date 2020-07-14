from collections import deque


MX = 10**4
S = int(input())
time = [9999] * MX

def bfs():
    q = deque([(1, 0, 0)])
    time[1] = 0

    while q:
        now, clip, t = q.popleft()
        if now == S:
            return

        if not(0 < now < MX):
            continue

        if time[now-1] > t+1:
            q.append((now-1, clip, t+1))
            time[now-1] = min(time[now-1], t + 1)

        if clip:
            q.append((now + clip, clip, t+1))
            time[now+clip] = min(time[now+clip], t + 1)

        if clip != now:
            q.append((now, now, t+1))

bfs()
print(time[S])