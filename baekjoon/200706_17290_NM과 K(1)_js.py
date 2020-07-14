def bj18290():
    n, m, k  = (int(i) for i in input().split(' '))
    board = []
    values = []
    max_sum = None
    for i in range(n):
        board.append([int(j) for j in input().split(' ')])
    print(board)

    def no_neighbor(i, j):
        for v in values:
            if v[0] == i:
                if (v[1]-j)**2 <= 1:
                    return False
            elif v[1] == j:
                if (v[0]-i)**2 <= 1:
                    return False
        return True


    def recur(count):
        nonlocal max_sum
        if len(values) == 0:
            start = (0,0)
        else:
            start = values[-1]
        print(values, count, k)
        if count == k:
            temp_max = 0
            for v in values:
                temp_max += board[v[0]][v[1]]
            if max_sum == None:
                max_sum = temp_max
            elif max_sum < temp_max:
                max_sum = temp_max
            return
        for i in range(start[0],n):
            for j in range(0,m):
                print(values,start,i,j)
                if no_neighbor(i, j):
                    values.append((i,j))
                    recur(count+1)
                    values.pop()
    recur(0)
    print(max_sum)
bj18290()