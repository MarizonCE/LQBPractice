"""
如果编号互质则不握手
"""
from math import gcd

# def gcd(n1, n2):
#     """
#     判断两个数是否互质
#     :param n1: 需要判断的数（小）
#     :param n2: 需要判断的数（大）
#     :return: 如果互质则返回True
#     """
#     if n2 == 0:
#         return n1
#     else:
#         return gcd(n2, n1 % n2)


ans = 0
for i in range(1, 51):
    for j in range(i + 1, 51):
        if i > 7 or j > 7:
            if gcd(i, j) == 1:
                ans += 1
print(ans)
