# # 解法1：
# """
# 失误1：不会求四舍五入
# 失误2：忘记导入math
# 失误3：忘记加上sqrt求平方根
# """
# from math import sqrt
#
# dx = 15
# dy = 17
# w = 343720
# h = 233333
#
# # 数学关系：dx/dy = (a*2w)/(b*2h),a和b为整数,则a = (dx*b*h)/(dy*w)
# # x = a*2w,y = b*2h
# y = 0  # y = 2*b*h,最终的高度
# a = 0  # 2*a为宽度系数
# b = 1  # 2*b为高度系数
# while True:
#     if (dx * b * h) % (dy * w) == 0:  # 找到符合条件的高度系数
#         a = (dx * b * h) // (dy * w)
#         y = 2 * b * h  # 最终的高度
#         break
#     b += 1
# x = 2 * a * w
# print(round(sqrt(x ** 2 + y ** 2), 2))
# print(f"{sqrt(x ** 2 + y ** 2):.2f}")
# print(format(sqrt(x ** 2 + y ** 2), ".2f"))

# 解法2：
import math

ans = 0
h = 233333
l = 343720
while True:
    if l / h > 15 / 17:
        h += 233333  # 如果球碰到底边就加1个单位高度，底边下移1个单位高度
    elif l / h < 15 / 17:
        l += 343720  # 如果求碰到右边就加1个单位长度，右边右移1个单位长度
    else:
        print(round(2*math.sqrt(l ** 2 + h ** 2), 2))  # 到达右下角后的距离的两倍
        break
