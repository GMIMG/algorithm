from collections import deque


N, K = map(int, input().split())
Max = 10**5+1
# dp = [0] * Max
dp = [-1]*Max
q = deque([(N,0)])

def bfs():
    while q:
        now, time = q.popleft()
        if now == K:
            return time
        for i in (now-1, now+1, now*2):
            if 0 <= i < Max and dp[i] == -1:
                q.append((i,time+1))
                dp[i] = now


print(bfs())

temp = []
next_idx = K
while next_idx != N:
    temp.append(next_idx)
    next_idx = dp[next_idx]
temp.append(N)
print(*reversed(temp))