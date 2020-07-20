N = int(input())
result = set()

# def dfs(now, depth):
#     if depth == N:
#         result.add(now)
#         return
#     for i in [50, 10, 5, 1]:
#         dfs(now+i, depth+1)
#
# dfs(0,0)
# print(len(result))


import itertools

for i in itertools.combinations_with_replacement([1,5,10,50], N):
    result.add(sum(i))
print(len(result))