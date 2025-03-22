# 输入正整数 N
N = int(input())

# 初始化全局最大值 Max 为 0
Max = 0

# 边界情况：如果 N == 1，直接输出 1（Collatz 序列中 1 的最大值为 1）
if N == 1:
    print(1)
else:
    # 遍历从 2 到 N 的所有正整数
    for i in range(2, N + 1):
        x = i
        # 计算 i 的 Collatz 序列，直到 x 变成 1
        while x != 1:
            # 如果 x 是偶数，除以 2
            if x % 2 == 0:
                x //= 2
            # 如果 x 是奇数，按 3x+1 规则计算
            else:
                x = x * 3 + 1
            # 更新当前遇到的最大值
            if x > Max:
                Max = x
            # 优化：如果 x 已经小于 i，说明这个序列后续路径已经被之前的 i 处理过，可以提前退出
            if x < i:
                break
    # 输出全局最大值
    print(Max)
