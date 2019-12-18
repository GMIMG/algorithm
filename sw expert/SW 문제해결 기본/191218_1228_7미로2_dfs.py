import sys


def dfs(nr, nc, depth, mx):
    # 최대깊이 저장
    if depth > mx:
        mx = depth
    # 막힌곳 이면 돌아감
    if input_lst[nr][nc] == 1:
        return 0
    # 도착했을 때
    if input_lst[nr][nc] == 3:
        # 도착지점을 저장하기위해 global 변수 이용
        # global er, ec
        # er = nr
        # ec = nc
        # 최대 깊이 출력
        # print(mx)
        return 1
    # 4방향으로 방문하지 않았다면 깊이 탐색
    for direction in range(4):
        if (nr + dr[direction], nc + dc[direction]) in visit:
            continue
        visit[(nr + dr[direction], nc + dc[direction])] = True
        if dfs(nr + dr[direction], nc + dc[direction], depth + 1, mx):
            return 1
    return 0


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 파이썬 재귀 깊이 세팅 (맵 탐색은 웬만하면 bfs가 나은듯)
if __name__ == '__main__':
    sys.setrecursionlimit(3000)

    for T in range(1, 11):
        t = int(input())
        input_lst = []
        sr = 0
        sc = 0
        for row in range(100):
            temp_lst = list(map(int, input()))
            if temp_lst.count(2):
                sc = temp_lst.index(2)
                sr = row
            input_lst.append(temp_lst)

        # 도착지점, 최대깊이, 방문장소 초기화
        er = 0
        ec = 0
        mx = 0
        visit = {(sr, sc): True}
        sol = dfs(sr, sc, 0, 0)
        print(f'#{T} {sol}')
        # print(er, ec)
