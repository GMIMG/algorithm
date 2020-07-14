from collections import deque

max = 10**8
S = int(input())
time = [-1] * max

def bfs():
    q = deque([(2, 1)])
    time[1] = 0
    time[2] = 2

    while q:
        # print(q)
        now, clip = q.popleft()
        for next, dt in ((now - 1, 1), (now + clip, 1), (now * 2, 2)):
            if 0 < next < max \
            and (time[next] == -1 or time[next] >= time[now] + dt):
                if next > S and (not now-1 == next):
                    continue
                if dt == 2:
                    clip = now
                time[next] = time[now] + dt
                q.append((next, clip))

bfs()
# print(time[:30])
print(time[S])