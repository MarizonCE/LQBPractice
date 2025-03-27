"""
该为十进制转十六进制，包含A,B,C,D,E,F
"""


def decimal_to_base_of_16(decimal: int, digits: str) -> str:
    """
    将输入的十进制数转换为用字符串表示的十六进制数
    :param decimal: 要转换的十进制整数
    :param digits: 规定的十六进制字符
    :return: 转换后的字符型十六进制整数
    """
    digit_list = []
    while decimal:
        digit_list.append(decimal % 16)
        decimal //= 16
    digit_list.reverse()
    for index, digit in enumerate(digit_list):
        if digit >= 10:
            digit_list[index] = digits[digit]
    base_of_16_value = "".join(map(str, digit_list))
    return base_of_16_value


digits_str = "0123456789ABCDEF"

# 输入需要转换的十进制数
num = int(input())

# 计算并转换十六进制数
base_of_16 = decimal_to_base_of_16(num, digits_str)
print(base_of_16)
