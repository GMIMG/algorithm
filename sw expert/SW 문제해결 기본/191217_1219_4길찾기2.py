import queue

for _ in range(10):
    (T, N) = map(int, input().split())
    input_lst = list(map(int, input().split()))
    dic = {}
    dic2 = {}
    while True:
        if not len(input_lst):
            break
        key = input_lst.pop(0)
        val = input_lst.pop(0)
        dic[key] = val
        if not len(input_lst):
            break
        key = input_lst.pop(0)
        val = input_lst.pop(0)
        dic2[key] = val

    que = queue.Queue()
    visit = {}
    que.put(0)
    visit[0] = True
    sol = 0

    while True:
        if not que.qsize() or sol:
            break
        now = que.get()

        if now in dic and dic[now] not in visit:
            que.put(dic[now])
            visit[dic[now]] = True
            # print(dic[now])
            if dic[now] == 99:
                sol = 1
        if now in dic2 and dic2[now] not in visit:
            que.put(dic2[now])
            visit[dic2[now]] = True
            # print(dic2[now])
            if dic2[now] == 99:
                sol = 1

    print(f'#{T} {sol}')
