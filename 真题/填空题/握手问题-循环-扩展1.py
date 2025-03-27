"""如果编号之和为偶数则不握手"""

ans = 0
for i in range(1,51):
    for j in range(i+1,51):
        if i>7 or j>7:
            if (i+j)%2 == 1:
                ans += 1
print(ans)