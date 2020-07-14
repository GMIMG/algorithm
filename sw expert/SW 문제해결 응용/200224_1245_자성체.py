NUM_TEST = int(input())
for test in range(NUM_TEST):
    N = int(input())
    lst_input = tuple(map(float, input().split()))
    x = lst_input[:N]
    m = lst_input[N:]
    ans = 0
    print(f'#{test+1}', end=' ')
    old_mid = 0
    for i in range(N-1):
        left = x[i]
        right = x[i + 1]
        while True:
            result = 0
            mid = (left + right) / 2
            for k in range(i + 1):
                result += m[k] / (mid - x[k])**2

            for k in range(i + 1, N):
                result -= m[k] / (mid - x[k])**2

            if result > 0:
                left = mid
            else:
                ans = mid
                right = mid

            if old_mid == round(mid,11):
                break
            else:
                old_mid = round(mid,11)
        print("%.10f" % ans, end=' ')
    print()