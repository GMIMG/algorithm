
for i in range(1,11):
    lst = []
    N = int(input())
    st_input = input()
    for idx in range(N):
        if st_input[idx] == ')' and lst[-1] == '(':
            lst.pop()
        elif st_input[idx] == ']' and lst[-1] == '[':
            lst.pop()
        elif st_input[idx] == '}' and lst[-1] == '{':
            lst.pop()
        elif st_input[idx] == '>' and lst[-1] == '<':
            lst.pop()
        else:
            lst.append(st_input[idx])
    if len(lst):
        sol = 0
    else :
        sol = 1

    print(f'#{i} {sol}')