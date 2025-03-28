"""
改成n进制转10进制
"""


# 将输入的数字拆分为列表，按从低位到高位排序
def split_digits(number):
    digits = []
    while number:
        digits.append(number % 10)  # 会先追加低数位
        number //= 10  # 去掉最低位
    return digits


# 主程序
def convert_to_decimal(base_from, number):
    result = 0
    for i, digit in enumerate(split_digits(number)):  # 从低到高位计算
        result += digit * base_from ** i  # 计算该位对应的十进制值
    return result


# 输入被转化数的进制和需要转化后的数的进制
n = int(input())
# 输入需要转换的数字
num = int(input())

# 计算并输出转换结果
decimal_value = convert_to_decimal(n, num)
print(decimal_value)

"""
decimal: 十进制
"""
