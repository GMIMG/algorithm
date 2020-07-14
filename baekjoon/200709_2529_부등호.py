import sys

k = int(sys.stdin.readline())
lst = tuple(sys.stdin.readline().split())

max_sol = []
min_sol = []
now1 = 9
now2 = 0
stack1 = 0
stack2 = 0


def add_max(now, stack):
    for i in range(now - stack + 1, now + 1):
        max_sol.append(i)

def add_min(now, stack):
    for i in range(stack):
        min_sol.append(now + stack - i - 1)

for l in lst:
    if l == '<':
        add_min(now2, stack2 + 1)
        now2 += stack2 + 1
        stack2 = 0
        stack1 += 1
    if l == '>':
        add_max(now1, stack1 + 1)
        now1 -= stack1 + 1
        stack1 = 0
        stack2 += 1

add_max(now1, stack1 + 1)
add_min(now2, stack2 + 1)
print(''.join(list(map(str, max_sol))))
print(''.join(list(map(str, min_sol))))


