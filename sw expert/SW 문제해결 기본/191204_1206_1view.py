T = 0
for t in range(10):
    T = T + 1
    N = int(input())
    s = 0
    lst = list(map(int, input().split()))
    for i in range(2, N - 2):
        m = min([lst[i] - lst[i-2], lst[i] - lst[i-1], lst[i] - lst[i+1], lst[i] - lst[i+2]])
        if m > 0:
            s = s + m
    print('#{}'.format(T), s)