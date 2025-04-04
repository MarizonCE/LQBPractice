"""
模板题：
给定一个n进制数s,请将其转换为m进制。(2≤n,m≤36)(用A~Z表示10~35）
例如：n=10,m=16,s=30,转换后得到的结果为1E.

步骤：
1. 先将n进制转换为10进制。
2. 再将10进制转换为m进制
"""

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert_to_decimal(source_base: int, number_str: str) -> int:
    """将 source_base 进制的字符串转换为十进制整数"""
    return int(number_str, source_base)


def convert_from_decimal(number: int, target_base: int) -> str:
    """
    将十进制整数转换为指定进制的字符串表示。
    """
    if number == 0:
        return "0"

    result = []  # 从低位到高位存储 target_base 进制的数字
    while number:
        remainder = number % target_base
        result.append(DIGITS[remainder])
        number //= target_base

    return ''.join(reversed(result))  # 反转列表并转换成字符串


def main():
    """读取输入，进行进制转换并输出结果。"""
    try:
        # 读取进制信息和待转换的数
        source_base, target_base = map(int, input("请输入 源进制 目标进制（用空格分割）：").split())
        number_str = input(f"请输入 {source_base} 进制的数：").strip().upper()

        # 检测进制范围是否有效
        if not (2 <= source_base <= 36 and 2 <= target_base <= 36):
            print("进制必须在2到36之间！")

        # 进制转换
        decimal_value = convert_to_decimal(source_base, number_str)
        target_value = convert_from_decimal(decimal_value, target_base)

        # 输出转换结果
        print(f"{number_str}（ {source_base} 进制）转换为 {target_base} 进制：{target_value}")

    except ValueError as e:
        print(f"输入错误：{e}")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    main()
