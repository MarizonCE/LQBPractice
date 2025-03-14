def input_list():
    # 读取一行输入，并将其转换为整数列表
    return list(map(int, input().split()))


# 输入列表的行数 n 和列数 m
n, m = input_list()
# 输入n行数据，存入列表a
a = [input_list() for _ in range(n)]

# 初始化结果列表，初始值为0
b = [[0] * m for _ in range(n)]
# 定义8个可能的相邻方向（左上、上、右上、左、右、左下、下、右下）
dire = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# 遍历列表中的每个元素
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            b[i][j] = 9  # 当前位置有地雷，设为9
        else:
            for dx, dy in dire:  # 遍历8个方向
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    b[i][j] += a[x][y]  # 计算周围地雷数
        print(b[i][j], end=' ')  # 按行输出
    print()  # 每行结束后换行
