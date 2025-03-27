# 解法1：
# print(50*49//2-7*6//2)

# 解法2：
# print(43*42//2+7*43)

# 解法3：
ans = 0
for i in range(1, 51):
    for j in range(i + 1, 51):
        if i > 7 or j > 7:
            ans += 1
print(ans)
