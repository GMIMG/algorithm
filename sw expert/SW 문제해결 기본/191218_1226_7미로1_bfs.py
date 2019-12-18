import queue


def bfs(que):
    # bfs 는 큐를 사용해서 탐색할위치가 끝날때까지 반복한다
    while True:
        # 큐 사이즈가 0 이면 while break
        if not que.qsize():
            break
        # 큐가 있으면 하나꺼내와서 현재 위치에 저장한다
        nr, nc = que.get()
        for direction in range(4):
            # 다음 위치를 방문하지 않았고 갈수 있는곳(0)이면 방문 체크한 뒤에 큐에 넣음
            if (nr + dr[direction], nc + dc[direction]) not in visit \
                    and not input_lst[nr + dr[direction]][nc + dc[direction]]:
                visit[(nr + dr[direction], nc + dc[direction])] = True
                que.put((nr + dr[direction], nc + dc[direction]))
            # 도착 위치(3)를 찾으면 큐를 끝냅니다
            if input_lst[nr + dr[direction]][nc + dc[direction]] == 3:
                # print(f'er{nr + dr[direction]}ec{nc + dc[direction]}')
                return 1
    return 0


# 위아래좌우 4방향을 쉽게 접근하기위해 table 로 만듭니다
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

for T in range(1, 11):
    t = int(input())
    input_lst = []
    sr = 0
    sc = 0
    for row in range(16):
        temp_lst = list(map(int, input()))
        # 시작위치(2) 찾기
        if temp_lst.count(2):
            sc = temp_lst.index(2)
            sr = row
        input_lst.append(temp_lst)
    # 큐를 생성하고 시작위치를 큐에 넣고 시작
    que = queue.Queue()
    que.put((sr, sc))
    visit = {(sr, sc): True}
    sol = bfs(que)
    print(f'#{T} {sol}')
