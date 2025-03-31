import sys


def f(x):
    if x > 10:
        return 2 * x * f(x - 6)
    elif x == 1:
        return 0
    else:
        return x * (x - 1)


sys.setrecursionlimit(100000)  # 提高递归深度限制
n = int(input())
print(f(n) % 998244353)
