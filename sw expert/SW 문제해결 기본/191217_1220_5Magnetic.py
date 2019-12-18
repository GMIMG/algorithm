for T in range(1, 11):
    N = int(input())
    input_map = []
    for row in range(100):
        input_map.append(list(map(int, input().split())))

    sol = 0
    for column in range(100):
        now = 0
        for row in range(100):
            if input_map[row][column]:
                if now == 1 and input_map[row][column] == 2:
                    sol += 1
                now = input_map[row][column]
    print(f'#{T} {sol}')