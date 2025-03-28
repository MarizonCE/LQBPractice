# 解法1：
# """
# 失误1：求YYYYMMDD格式的汉字笔画总数时，直接将其对应的数字相加了，没有转换为汉字
# 失误2：更改闰年的二月天数时，直接永久性更改了
# 失误3：函数外部的变量名与函数名冲突了，造成‘int' is not callable报错
# """
#
#
# def bihua_sum(date):
#     """
#     将字符串型的日期转换为对应汉字并对其笔画求和
#     :param date: 字符串型，YYYYMMDD格式的日期
#     :return: int型，将字符串型的日期转换为对应汉字并对其笔画求和的结果
#     """
#     sum = 0
#     for d in date:
#         sum += bihuas[int(d)]
#     return sum
#
#
# # 0~9每个汉字的笔画
# bihuas = [13, 1, 2, 3, 5, 4, 4, 2, 2, 2]
#
# # 初始化练习篮球的总天数
# lanqiu = 0
#
# for year in range(2000, 2025):  # 先遍历从2000年到2023年的所有日期情况，后续再对2024年进行特殊计算
#     # 非闰年1~12月中每个月的天数
#     mds = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 对于闰年的情况，后续使用mds[1]=29处理
#     if year != 2024:
#         for month in range(1, 13):
#             if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#                 mds[1] = 29
#             for day in range(1, mds[month - 1] + 1):
#                 year_str = str(year)
#                 mon_str = str(month)
#                 if len(mon_str) == 1:  # 如果月数是个位数要在前面加上0的形式
#                     mon_str = '0' + mon_str
#                 day_str = str(day)
#                 if len(day_str) == 1:
#                     day_str = '0' + day_str
#                 date_str = year_str + mon_str + day_str
#                 bihua_value = bihua_sum(date_str)
#                 if bihua_value > 50:
#                     lanqiu += 1
#     else:
#         for month in range(1, 5):
#             if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#                 mds[1] = 29
#             if month != 4:
#                 for day in range(1, mds[month - 1] + 1):
#                     year_str = str(year)
#                     mon_str = str(month)
#                     mon_str = '0' + mon_str
#                     day_str = str(day)
#                     if len(day_str) == 1:
#                         day_str = '0' + day_str
#                     date_str = year_str + mon_str + day_str
#                     bihua_value = bihua_sum(date_str)
#                     if bihua_value > 50:
#                         lanqiu += 1
#             else:
#                 for day in range(1, 14):
#                     year_str = str(year)
#                     mon_str = str(month)
#                     mon_str = '0' + mon_str
#                     day_str = str(day)
#                     if len(day_str) == 1:
#                         day_str = '0' + day_str
#                     date_str = year_str + mon_str + day_str
#                     bihua_value = bihua_sum(date_str)
#                     if bihua_value > 50:
#                         lanqiu += 1
#
# print(lanqiu)


# 解法2：
# """
# 失误1：more_than_50函数中是对笔画进行求和，而不是日期的每一位数
# 失误2：改一个地方可能会牵动其他地方，记得也要改
# 失误3；对天数进行循环时是range(1, days_month[month_cir - 1] + 1)，而不是range(1,day_month[month_cir] +1),会越界
# """
# """
# 1.循环每一天，将该天所在日期转换成“YYYYMMDD”格式
# 2. 输入“YYYYMMDD”格式的日期，判断是否每位数之和是否大于50
# """
#
#
# def date_format(year: int, month: int, day: int) -> str:
#     """
#     将年月日转换为“YYYYMMDD”格式
#     :param year: int型年份
#     :param month: int型月份
#     :param day: int型天数
#     :return: “YYYYMMDD”格式的字符串
#     """
#     month_str = f"0{month}" if 1 <= month < 10 else str(month)
#     day_str = f"0{day}" if 1 <= day < 10 else str(day)
#     date_str = str(year) + month_str + day_str
#
#     return date_str
#
#
# def more_than_50(date_str: str, strokes: list) -> bool:
#     cnt = 0
#     for digit in date_str:
#         cnt += strokes[int(digit)]
#         if cnt > 50:
#             return True
#     return False
#
#
# # 零到九每个汉字的笔画数
# strokes_init = [13, 1, 2, 3, 5, 4, 4, 2, 2, 2]
# # 非闰年每个月的天数
# days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# # 输入统计的开始日期
# date_start = (2000, 1, 1)
# # 输入统计的结束日期
# date_end = (2024, 4, 13)
#
# # 初始化练习篮球的天数为0
# days = 0
#
# # 计算并输出结果
# # 遍历每一年
# for year_cir in range(date_start[0], date_end[0] + 1):
#
#     # 判断是否为闰年，闰年将二月改为29天，否则改回28天
#     if (year_cir % 4 == 0 and year_cir % 100 != 0) or year_cir % 400 == 0:
#         days_month[1] = 29
#     else:
#         days_month[1] = 28
#
#     if year_cir == 2024:  # 2024年的情况
#         for month_cir in range(1, 5):
#             if month_cir == 4:  # 4月的情况
#                 for day_cir in range(1, 14):
#                     if more_than_50(date_format(year_cir, month_cir, day_cir), strokes_init):
#                         days += 1
#             else:  # 不是4月的情况
#                 for day_cir in range(1, days_month[month_cir - 1] + 1):
#                     if more_than_50(date_format(year_cir, month_cir, day_cir), strokes_init):
#                         days += 1
#     else:  # 不是2024年的情况
#         for month_cir in range(1, 13):
#             for day_cir in range(1, days_month[month_cir - 1] + 1):
#                 if more_than_50(date_format(year_cir, month_cir, day_cir), strokes_init):
#                     days += 1
# print(days)

# 解法3：
import datetime

date_start = datetime.date(2000, 1, 1)  # 开始日期，格式为：2000-01-01
date_end = datetime.date(2024, 4, 13)  # 结束日期
day = datetime.timedelta(days=1)  # 时间间隔，可与datetime.date类型数据运算
strokes_init = [13, 1, 2, 3, 5, 4, 4, 2, 2, 2]  # 零到九的汉字笔画数
days = 0  # 练习篮球的天数
while date_start <= date_end:
    date = map(int, list(str(date_start).replace('-', "")))
    ans = 0
    for d in date:
        ans += strokes_init[d]
    if ans > 50:
        days += 1
    date_start += day
print(days)
