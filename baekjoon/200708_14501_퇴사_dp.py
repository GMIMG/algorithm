import sys

N = int(sys.stdin.readline())
dp = [0]*20

for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    dp[i + 1] = max(dp[i], dp[i + 1])
    dp[i + t] = max(dp[i + t], dp[i] + p)

print(max(dp[:N+1]))