# def change(n, m, s):
#     """
#
#     :param n:
#     :param m:
#     :param s:
#     :return:
#     """
#     res = 0
#     for i in s:
#         res = res * n + (int(i) if i.isdight() else (ord(i) - ord('A') + 10))
#     ans = ""
#     while res > 0:
#         x = res % m
#         if 10 <= x < 15:
#             ans += chr(ord('A') + x - 10)
#         else:
#             ans += str(x)
#         res //= m
#     return ans[::-1]
#
#
# n, m, s = map(int, input().split())
# print(change(n, m, s))
