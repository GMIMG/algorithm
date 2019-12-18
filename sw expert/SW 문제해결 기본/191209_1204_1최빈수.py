T = int(input())
for test in range(T):
    N = int(input())
    tu = tuple(map(int, input().split()))
    dic = dict()
    for num in tu:
        if num not in dic:
            dic[num] = 0
        dic[num] = dic[num] + 1
    m = max(dic.values())
    for i in range(100, 0, -1):
        if i in dic and dic[i] == m:
            print('#{}'.format(N), i)
            break
