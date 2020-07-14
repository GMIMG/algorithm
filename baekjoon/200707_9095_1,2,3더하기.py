T = int(input())


def solution(n):
    sol = [1, 2, 4]
    for i in range(4, 12):
        sol.append(sum(sol[-3:]))
    return sol[n-1]


for i in range(T):
    print(solution(int(input())))