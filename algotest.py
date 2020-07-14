# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
TEST = int(input())
row, col = tuple(map(int,input().split()))
coord = []
for _ in range(row):
	coord.append(list(map(int,input().split())))

T_coord = [x for x in zip(*coord)]

if 0 in coord[1] or 0 in coord[row-1]:
	print('NO')

elif 0 in T_coord[1] or 0 in T_coord[row-1]:
    print('NO')
print(T_coord)
