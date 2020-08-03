N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dd = (3,0,1,2)
dr = (-1,0,1,0)
dc = (0,1,0,-1)

result = 0

while True:
    # 청소하기
    if board[r][c] != 2:
        result += 1
        board[r][c] = 2

    # 주변 청소할 곳을 확인
    flag = 0
    for _ in range(4):
        d = dd[d]
        nextr, nextc = r+dr[d], c+dc[d]
        # 청소할 공간이 없을때
        if board[nextr][nextc]:
            continue
        # 청소할 공간이 있을때
        else:
            r = nextr
            c = nextc
            flag = 1
            break
    if flag:
        continue

    # 후진
    if board[r - dr[d]][c - dc[d]] == 1:
        break
    else:
        r, c = r - dr[d], c - dc[d]


# temp = 0
# for i in range(N):
#     print(board[i])
#     for j in range(M):
#         if board[i][j] == 2:
#             temp +=1
# print(temp)

print(result)