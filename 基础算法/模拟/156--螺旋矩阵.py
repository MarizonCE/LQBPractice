# 定义输入函数，读取一行输入并返回多个整数
def input_list():
    return map(int, input().split())


# 输入矩阵的行数n和列数m
n, m = input_list()

# 输入需要查询的坐标r和c
r, c = input_list()

# 初始化结果矩阵，初始值全为0
Map = [[0] * m for _ in range(n)]

# 初始化起点和填充值
value = 1
x, y = 0, 0
Map[x][y] = value  # 填充起点

# 持续填充直到value达到n*m
while value < n * m:

    # 向右填充
    while y + 1 < m and Map[x][y + 1] == 0:
        y += 1
        value += 1
        Map[x][y] = value

    # 向下填充
    while x + 1 < n and Map[x + 1][y] == 0:
        x += 1
        value += 1
        Map[x][y] = value

    # 向左填充
    while y - 1 >= 0 and Map[x][y - 1] == 0:
        y -= 1
        value += 1
        Map[x][y] = value

    # 向上填充
    while x - 1 >= 0 and Map[x - 1][y] == 0:
        x -= 1
        value += 1
        Map[x][y] = value

# 输出目标位置的值
print(Map[r - 1][c - 1])  # 注意不要写成Map[r][c]了，要求第r行第c列
