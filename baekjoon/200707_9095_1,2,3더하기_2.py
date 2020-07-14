T = int(input())


def recur(n):
    if n == 1:
        dp[0] = 1
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if dp[n-1]:
        return dp[n-1]
    else:
        dp[n - 1] = recur(n - 3) + recur(n - 2) + recur(n - 1)
        return dp[n-1]

dp = [0]*11
dp[0] = 1
dp[1] = 2
dp[2] = 4

def solution(n):
    result = recur(n)
    return result


for i in range(T):
    print(solution(int(input())))