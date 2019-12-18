import queue

for _ in range(10):
    T, N = map(int, input().split())


    input_lst = list(map(int, input().split()))
    route = []
    for idx in range(N):
        route.append((input_lst.pop(0), input_lst.pop(0)))
    # print(route)


    que = queue.Queue()
    visit = {}
    que.put(0)
    visit[0] = True
    sol = 0

    while True:
        if not que.qsize() or sol:
            break
        now = que.get()
        for r in route:
            if (r[0] == now) & (r[1] not in visit):
                que.put(r[1])
                visit[r[1]] = True
                # print(r[1])
                if r[1] == 99:
                    sol = 1
    print(f'#{T} {sol}')
