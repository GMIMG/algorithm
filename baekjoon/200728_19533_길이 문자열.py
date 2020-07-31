def sol(a,b):
    length_a = len(str(a))
    if length_a + b < 3:
        num = a*(10**b)
        stack = []
        # old_len = len(str(num))
        while True:
            stack.append(num)
            num -= len(str(num))+1
            # if len(str(num)) != old_len:
            #     print(num)
            # old_len = len(str(num))
            if num == 0:
                temp_str = ''
                while stack:
                    temp_str += '-' + str(stack.pop())
                if len(temp_str) >= 21:
                    print(temp_str[:17] + '...')
                else:
                    print(temp_str)
                return
            elif num == -1:
                temp_str = ''
                while stack:
                    temp_str += str(stack.pop()) + '-'
                temp_str = temp_str[:-1]
                if len(temp_str) >= 21:
                    print(temp_str[:17] + '...')
                else:
                    print(temp_str)
                return

    a1 = a - 10 ** (length_a - 1)
    start = a1 * (10 ** b) % (length_a+b +1)
    num = (10 ** (length_a+b-1)) + start - (length_a+b+1)
    while True:
        print(num)
        len_num = len(str(num))
        if len_num < 3:
            if num % 10 == 8:
                print('-2-4-6-8-11-14-17...')
                break
            elif num % 10 == 7:
                print('1-3-5-7-10-13-16-...')
                break
            else:
                print('1-3-5-7-9-12-15-1...')
                break
        else:
            b = len_num - 1
            num = 10**b + (num - 10**b) % (len_num + 1) - (len_num+1)


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    sol(a, b)

