# 输入矩阵的行数n和列数m
n, m = list(map(int, input().split()))

# 初始化结果矩阵ans，包含n个空列表
ans = [[] for _ in range(n)]

# 读取原始像素矩阵Map  # 二维列表要这样生成，不能：ma = [list(map(int, input().split()) for _ in range(n))]
Map = [list(map(int, input().split())) for _ in range(n)]
# for _ in range(n):
#     ma = list(map(int, input().split()))
#     Map.append(ma)

# 遍历原始像素矩阵的每个像素点
for i in range(n):
    for j in range(m):
        tot, cnt = 0, 0  # tot：3*3范围内像素值的总和，cnt：实际参与计算的像素点个数

        # 遍历当前像素的3*3邻域
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x, y = i + dx, j + dy
                # 判断邻域内的像素是否越界
                if 0 <= x < n and 0 <= y < m:
                    tot += Map[x][y]
                    cnt += 1
        # 将当前像素的均值（向下取整）添加到结果矩阵
        ans[i].append(tot // cnt)

# 输出结果矩阵
for a in ans:
    print(" ".join(map(str, a)))  # 注意是join，不是joint
