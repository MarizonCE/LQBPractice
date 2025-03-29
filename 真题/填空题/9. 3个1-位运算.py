def ten_to_two(n):
    """
    将十进制转换为二进制，并放入列表中
    :param n: 需要转换的十进制数字
    :return: 返回二进制列表
    """
    # while n != 0:
    #     if n % 2 == 1:
    #         num_two_list.append(1)
    #     else:
    #         num_two_list.append(0)
    #     n //= 2
    num_two_list = [i for i in bin(n)[2:]]

    return num_two_list


def just_111(num_two_list):
    """
    判断二进制列表是否恰好包含3个1
    :param num_two_list: 需要判断的二进制列表
    :return: 如果符合要求，返回True
    """
    tot = num_two_list.count('1')
    # tot = 0
    # for num in num_two_list:
    #     if num == 1:
    #         tot += 1
    if tot == 3:
        return True
    else:
        return False


cnt = 0  # 恰好包含3个1的二进制个数
number = 7  # 从十进制7开始遍历
while cnt < 23:
    if just_111(ten_to_two(number)):
        cnt += 1
    number += 1

print(number - 1)
