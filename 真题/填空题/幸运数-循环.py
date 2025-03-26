"""
绊脚石：不会优化，导致运行超时
"""


def two_half(num):
    """
    将数字切分成数位相等的两半
    :param num: 需要切分的数字（偶数位的数）
    :return: 两个字符串列表，第一个是前半部分的数字，第二个是后半部分的数字
    """
    st = str(num)
    length = len(st)  # 判断输入数字的数位是多少？
    mid = length // 2
    st1 = st[0:mid]  # 前半部分数字的字符串形式
    st2 = st[mid + 1:]  # 后半部分数字的字符串形式
    return st1, st2


def equality(st1, st2):
    """
    判断前一半数位之和十分偶等于后一半数位之和
    :param st1: 前一半数字的字符串形式
    :param st2: 后一半数字的字符串形式
    :return: 如果前一半数位之和十分偶等于后一半数位之和相等则返回True
    """
    before = sum(int(s) for s in st1)  # 前一半数位求和
    after = sum(int(s) for s in st2)  # 后一半数位求和
    if before == after:
        return True


cnt = 0
for i in range(10, 100):
    if len(str(i)) % 2 == 0:
        string1, string2 = two_half(i)
        if equality(string1, string2):
            cnt += 1
for i in range(1000, 10000):
    if len(str(i)) % 2 == 0:
        string1, string2 = two_half(i)
        if equality(string1, string2):
            cnt += 1
for i in range(100000, 1000000):
    if len(str(i)) % 2 == 0:
        string1, string2 = two_half(i)
        if equality(string1, string2):
            cnt += 1
for i in range(10000000, 100000000):
    if len(str(i)) % 2 == 0:
        string1, string2 = two_half(i)
        if equality(string1, string2):
            cnt += 1

print(cnt)
