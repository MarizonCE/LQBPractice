"""
改为n进制转为m进制(n,m<=10)
"""


# 将输入的数字拆分为列表，按从低位到高位排序
def split_digits(number):
    digits = []
    while number:
        digits.append(number % 10)  # 会先追加低数位
        number //= 10  # 去掉最低位
    return digits


# 将已拆分的数字列表转化为十进制
def convert_to_decimal(base_from, number):
    result = 0
    for i, digit in enumerate(split_digits(number)):  # 从低到高位计算
        result += digit * base_from ** i  # 计算该位对应的十进制值
    return result


# 将十进制转换为m进制
def decimal_to_m_base(base_to, decimal):
    m_base_list = []
    while decimal:
        m_base_list.append(decimal % base_to)
        decimal //= base_to
    m_base_list.reverse()
    m_base_dight = int("".join(map(str, m_base_list)))
    return m_base_dight

# 输入被转化数的进制和需要转化后的数的进制
n, m = map(int, input().split())
# 输入需要转换的数字
num = int(input())

# 计算并输出转换结果
decimal_value = convert_to_decimal(n, num)  # 转换为十进制
m_base_value = decimal_to_m_base(m, decimal_value)  # 十进制转换为m进制
print(m_base_value)
