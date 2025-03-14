import os
import sys


# 请在此输入您的代码
def input_list():
    return list(map(int, input().split()))


n, m = input_list()
a = []
for i in range(n):
    a.append(input_list())
b = [[0] * m for _ in range(n)]

dire = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            b[i][j] = 9
        else:
            for k in range(8):
                x, y = i + dire[k][0], j + dire[k][1]
                if 0 <= x < n and 0 <= y < m:
                    b[i][j] += a[x][y]
        print(b[i][j], end=' ')
    print()
