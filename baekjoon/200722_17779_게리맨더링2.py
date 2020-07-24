def sol(x,y,d1,d2):
    area = [0]*5
    if x + d1 + d2 >= N or y - d1 < 0 or y + d2 >= N:
        return
    for r in range(N):
        if r < x:
            area[0] += sum(board[r][:y+1])
            area[1] += sum(board[r][y+1:])
        elif r > x + d1+d2:
            area[2] += sum(board[r][:y])
            area[3] += sum(board[r][y:])
        else:
            mn_d, mx_d = (d1, d2) if d1 < d2 else (d2, d1)

            if x <= r < x + mn_d:
                area[0] += sum(board[r][:y + 1 - (r - x)])
                area[4] += sum(board[r][y + 1 - (r - x) : y + 1 + (r - x) + 1])
                area[1] += sum(board[r][y + 1 + (r - x) + 1:])

            elif x + mx_d < r <= x + d1+d2:
                area[2] += sum(board[r][:y - (N - r)])
                area[4] += sum(board[r][y - (N - r) : y + (N - r)])
                area[3] += sum(board[r][:y + (N - r)])

            elif x + mn_d <= r <= x + mx_d:
                if d1 < d2:
                    area[2] += sum(board[r][:y - (r-mn_d) - mn_d + 1])
                    area[4] += sum(board[r][y - (r-mn_d) - mn_d: y - (r-mn_d) + mn_d + 1])
                    area[1] += sum(board[r][y - (r-mn_d) + mn_d + 1:])
                elif d1 > d2:
                    area[0] += sum(board[r][:y + (r-mn_d) - mn_d + 1])
                    area[4] += sum(board[r][y + (r-mn_d) - mn_d: y + (r-mn_d) + mn_d + 1])
                    area[3] += sum(board[r][y - (r-mn_d) + mn_d + 1:])
                elif d1 == d2:
                    area[2] += sum(board[r][:y - (r - x)])
                    area[4] += sum(board[r][y - (r - x):y + (r - x) + 1])
                    area[1] += sum(board[r][y + (r - x) + 1 + 1:])
    print(x,y,d1,d2)
    print(area)
    return max(area) - min(area)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = set()
for x in range(N):
    for y in range(N):
        for d1 in range(N):
            for d2 in range(N):
                r = sol(x,y,d1,d2)
                if r:
                    result.add(r)
print(min(result))