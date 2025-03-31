# 解法1：
# ans = 0
#
# for i in range(1, 2021):
#     w_list = str(i)
#     if '2' in w_list:
#         for w in w_list:
#             if w == '2':
#                 ans += 1
#
# print(ans)

# 解法2：
def f(n):
    a = []
    while n != 0:
        a.append(n % 10)
        n //= 10
    ans = a.count(2)
    return ans


res = 0
if __name__ == "__main__":
    for i in range(1, 2021):
        res += f(i)
print(res)
