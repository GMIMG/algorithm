for test_case in range(1, 10 + 1):
    T = int(input())
    input_lst = []
    for row in range(100):
        input_lst.append(list(map(int, input().split())))
    max_sum_value = 0

    # 열값의 합
    for row in range(100):
        sum_value = 0
        for column in range(100):
            sum_value += input_lst[row][column]
        if max_sum_value < sum_value:
            max_sum_value = sum_value
    # 행값의 합
    for column in range(100):
        sum_value = 0
        for row in range(100):
            sum_value += input_lst[row][column]
        if max_sum_value < sum_value:
            max_sum_value = sum_value

    # 대각선 1
    sum_value = 0
    for rc in range(100):
        sum_value += input_lst[rc][rc]
        if max_sum_value < sum_value:
            max_sum_value = sum_value

    # 대각선 2
    sum_value = 0
    for rc in range(100):
        sum_value += input_lst[rc][99 - rc]
        if max_sum_value < sum_value:
            max_sum_value = sum_value

    print('#{}'.format(T), max_sum_value)
