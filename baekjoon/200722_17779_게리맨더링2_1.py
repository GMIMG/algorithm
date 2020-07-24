def sol(x,y,d1,d2):
    area = [0]*5
    if x + d1 + d2 >= N or y - d1 < 0 or y + d2 >= N:
        return
    s = 0
    for row in board:
        s += sum(row)
    line = {}
    for i in range(d1+1):
        if x+i not in line:
            line[x+i] = [y-i]
        else:
            line[x+i].append(y-i)
        if x+d2+i not in line:
            line[x+d2+i] = [y+d2-i]
        else:
            line[x+d2+i].append(y+d2-i)
    for i in range(d2+1):
        if x+i not in line:
            line[x+i] = [y+i]
        else:
            line[x+i].append(y+i)
        if x+d1+i not in line:
            line[x+d1+i] = [y-d1+i]
        else:
            line[x+d1+i].append(y-d1+i)
    # print(line)

    for r in range(N):
        for c in range(N):
            if r < x+d1 and c <= y and c < min(line.get(r, [N+1])):
                area[0] += board[r][c]
            elif r <= x+d2 and y < c <= N and c > max(line.get(r, [-1])):
                area[1] += board[r][c]
            elif x+d1 <= r <= N and c < y-d1+d2 and c < min(line.get(r, [N+1])):
                area[2] += board[r][c]
            elif x+d2 < r <= N and y-d1+d2 <= c <= N and c > max(line.get(r, [-1])):
                area[3] += board[r][c]
    area[4] = s-sum(area)
    # print(x,y,d1,d2)
    # print(area)
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