"""
失误1：求YYYYMMDD格式的汉字笔画总数时，直接将其对应的数字相加了，没有转换为汉字
失误2：更改闰年的二月天数时，直接永久性更改了
失误3：函数外部的变量名与函数名冲突了，造成‘int' is not callable报错
"""


def bihua_sum(date):
    """
    将字符串型的日期转换为对应汉字并对其笔画求和
    :param date: 字符串型，YYYYMMDD格式的日期
    :return: int型，将字符串型的日期转换为对应汉字并对其笔画求和的结果
    """
    sum = 0
    for d in date:
        sum += bihuas[int(d)]
    return sum


# 0~9每个汉字的笔画
bihuas = [13, 1, 2, 3, 5, 4, 4, 2, 2, 2]

# 初始化练习篮球的总天数
lanqiu = 0

for year in range(2000, 2025):  # 先遍历从2000年到2023年的所有日期情况，后续再对2024年进行特殊计算
    # 非闰年1~12月中每个月的天数
    mds = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 对于闰年的情况，后续使用mds[1]=29处理
    if year != 2024:
        for month in range(1, 13):
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                mds[1] = 29
            for day in range(1, mds[month - 1] + 1):
                year_str = str(year)
                mon_str = str(month)
                if len(mon_str) == 1:  # 如果月数是个位数要在前面加上0的形式
                    mon_str = '0' + mon_str
                day_str = str(day)
                if len(day_str) == 1:
                    day_str = '0' + day_str
                date_str = year_str + mon_str + day_str
                bihua_value = bihua_sum(date_str)
                if bihua_value > 50:
                    lanqiu += 1
    else:
        for month in range(1, 5):
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                mds[1] = 29
            if month != 4:
                for day in range(1, mds[month - 1] + 1):
                    year_str = str(year)
                    mon_str = str(month)
                    mon_str = '0' + mon_str
                    day_str = str(day)
                    if len(day_str) == 1:
                        day_str = '0' + day_str
                    date_str = year_str + mon_str + day_str
                    bihua_value = bihua_sum(date_str)
                    if bihua_value > 50:
                        lanqiu += 1
            else:
                for day in range(1, 14):
                    year_str = str(year)
                    mon_str = str(month)
                    mon_str = '0' + mon_str
                    day_str = str(day)
                    if len(day_str) == 1:
                        day_str = '0' + day_str
                    date_str = year_str + mon_str + day_str
                    bihua_value = bihua_sum(date_str)
                    if bihua_value > 50:
                        lanqiu += 1

print(lanqiu)
