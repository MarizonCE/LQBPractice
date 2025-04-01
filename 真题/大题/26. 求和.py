def total(lis):
    total_sum = sum(lis)
    return (total_sum * total_sum - sum(x * x for x in lis)) // 2


input()  # 省略不必要的 `n`
print(total(list(map(int, input().split()))))
