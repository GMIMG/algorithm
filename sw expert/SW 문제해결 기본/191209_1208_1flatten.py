T = 0
for _ in range(10):
    T = T + 1
    dump = int(input())
    lst = list(map(int, input().split()))
    for i in range(dump):
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1
        dt = max(lst) - min(lst)
        if dt == 1:
            break
    print('#{}'.format(T), dt)
