def oper(now, operation, operand):
    if operation == '+':
        return now + operand
    elif operation == '-':
        return now - operand
    elif operation == '*':
        return now * operand


def dfs(idx, now):
    if idx == N-1:
        result.append(now)
        return
    dfs(idx+2, oper(now, lst[idx+1], lst[idx+2]))
    if idx < N-4:
        dfs(idx+4, oper(now, lst[idx+1], oper(lst[idx+2], lst[idx+3], lst[idx+4])))


N = int(input())
mod = input()
result = []

lst = [int(i) if '0' <= i <= '9' else i for i in mod]

dfs(0, int(mod[0]))
print(max(result))