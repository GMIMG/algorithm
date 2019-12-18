def search(max_sol_col, input_lst):
    for row in range(100):
        # 100개부터 비교
        for sol_col in range(100, 0, -1):
            # 현재는
            for now in range(100 - sol_col + 1):
                solved = True
                for c in range(sol_col // 2):
                    if input_lst[row][now + c] != input_lst[row][-1 * (100 - sol_col - now + c + 1)]:
                        solved = False
                        break

                if solved:
                    if max_sol_col < sol_col:
                        # print(row, now, input_lst[row][now:now + sol_col], sol_col)
                        max_sol_col = sol_col
    return max_sol_col


for _ in range(10):
    test_case = input()
    input_lst = []
    for r in range(100):
        input_lst.append(list(input()))
    max_sol_col = 0
    max_sol_col = search(max_sol_col, input_lst)
    input_lst = list(map(list,zip(*input_lst)))
    max_sol_col = search(max_sol_col, input_lst)
    print(f'#{test_case} {max_sol_col}')
