# 输入数列的个数n
n = int(input())

# 输入数列，放入列表a_list中
a_list = list(map(int, input().split()))

# 初始化元素之间最大的元素距离为0
x = 0

for i, a in enumerate(a_list):
    for j, b in enumerate(a_list):
        if j > i:  # 避免重复计算
            d = (j - i) + abs(a - b)  # 计算距离
            x = max(x, d)  # 更新x

# 输出元素之间最大的元素距离
print(x)
