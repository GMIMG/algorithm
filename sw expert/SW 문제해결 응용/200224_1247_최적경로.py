def dfs(depth, distance, before, sol):
    if sol < distance:
        return sol
    if depth == N:
        distance += (abs(before[0] - house[0]) + abs(before[1] - house[1]))
        return distance

    for i in range(N):
        if i in visit: continue
        visit[i] = True
        d = dfs(depth + 1, distance + (abs(before[0] - customer[i][0]) + abs(before[1] - customer[i][1])), (customer[i][0],customer[i][1]), sol)
        if d < sol:
            sol = d
        del visit[i]
    return sol


NUM_TEST = int(input())
for test in range(NUM_TEST):
    N = int(input())
    input_lst = list(map(int, input().split()))
    customer = []
    company = (input_lst[0], input_lst[1])
    house = (input_lst[2], input_lst[3])
    for i in range(N):
        customer.append((input_lst[4 + i * 2], input_lst[5 + i * 2]))
    visit = {}
    print(f'#{test+1}', dfs(0, 0, company, 99999999))