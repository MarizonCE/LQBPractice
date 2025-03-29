# 解法1
# cnt = 0
# num = 2024
# while num != 0:
#     if num%2 == 1:
#         cnt += 1
#     num //= 2
#
# print(cnt)

# 解法2
print(bin(2024).count('1'))