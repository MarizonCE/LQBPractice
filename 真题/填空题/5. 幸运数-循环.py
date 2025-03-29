# """
# 绊脚石：不会优化，导致运行超时
# """
#
#
# def two_half(num):
#     """
#     将数字切分成数位相等的两半
#     :param num: 需要切分的数字（偶数位的数）
#     :return: 两个字符串列表，第一个是前半部分的数字，第二个是后半部分的数字
#     """
#     st = str(num)
#     length = len(st)  # 判断输入数字的数位是多少？
#     mid = length // 2
#     st1 = st[0:mid]  # 前半部分数字的字符串形式
#     st2 = st[mid + 1:]  # 后半部分数字的字符串形式
#     return st1, st2
#
#
# def equality(st1, st2):
#     """
#     判断前一半数位之和十分偶等于后一半数位之和
#     :param st1: 前一半数字的字符串形式
#     :param st2: 后一半数字的字符串形式
#     :return: 如果前一半数位之和十分偶等于后一半数位之和相等则返回True
#     """
#     before = sum(int(s) for s in st1)  # 前一半数位求和
#     after = sum(int(s) for s in st2)  # 后一半数位求和
#     if before == after:
#         return True
#
#
# cnt = 0
# for i in range(10, 100):
#     if len(str(i)) % 2 == 0:
#         string1, string2 = two_half(i)
#         if equality(string1, string2):
#             cnt += 1
# for i in range(1000, 10000):
#     if len(str(i)) % 2 == 0:
#         string1, string2 = two_half(i)
#         if equality(string1, string2):
#             cnt += 1
# for i in range(100000, 1000000):
#     if len(str(i)) % 2 == 0:
#         string1, string2 = two_half(i)
#         if equality(string1, string2):
#             cnt += 1
# for i in range(10000000, 100000000):
#     if len(str(i)) % 2 == 0:
#         string1, string2 = two_half(i)
#         if equality(string1, string2):
#             cnt += 1
# print(cnt)

# def equality(num):
#     """
#     判断数字的前半部分数位之和是否等于后半部分数位之和
#     :param num: 需要检查的数字
#     :return: 如果前一半数位之和等于后一半数位之和则返回True
#     """
#     length = len(str(num))  # 获取数字的位数
#     mid = length // 2
#
#     # 分别计算前半部分和后半部分的数位之和
#     before = sum(int(digit) for digit in str(num)[:mid])
#     after = sum(int(digit) for digit in str(num)[mid:])
#
#     return before == after
#
#
# # 统计符合条件的数字数量
# cnt = 0
# # 遍历范围，逐个检查每个偶数位数字
# for i in range(10, 100000000):
#     if len(str(i)) % 2 == 0 and equality(i):
#         cnt += 1
#
# print(cnt)

# def dfs(left, right, pos, length):
#     """
#     通过回溯构造符合条件的数字
#     :param left: 当前前半部分的数位和
#     :param right: 当前后半部分的数位和
#     :param pos: 当前位置
#     :param length: 数字的总长度
#     """
#     global cnt
#     if pos == length:
#         if left == right:
#             cnt += 1
#         return
#
#     for digit in range(10):
#         if pos < length // 2:
#             dfs(left + digit, right, pos + 1, length)
#         else:
#             dfs(left, right + digit, pos + 1, length)
#
#
# cnt = 0
# for length in range(2, 9, 2):  # 2, 4, 6, 8位数
#     dfs(0, 0, 0, length)
#
# print(cnt)

def chk(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    length = len(digits)
    if length % 2 != 0:
        return 0
    total = 0
    for i in range(length):
        if i < length // 2:
            total += digits[i]
        else:
            total -= digits[i]
    return 1 if total == 0 else 0

def chk1(x):
    s = str(x)
    n = len(s)
    if n % 2 != 0:
        return 0
    sum_left = sum(int(c) for c in s[:n//2])
    sum_right = sum(int(c) for c in s[n//2:])
    return 1 if sum_left == sum_right else 0

count = 0
for i in range(1, 10**8 + 1):
    if chk1(i):
        count += 1
print(count)