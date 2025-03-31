def henoi(num, source, auxiliary, target):
    global cnt
    if num == 1:  # 终止条件
        cnt += 1
        if cnt == m:
            print(f"#{1}: {source}->{target}")
        return
    else:
        henoi(num - 1, source, target, auxiliary)  # 先将A上面的num-1个圆盘移到B上
        cnt += 1  # 再将第num个圆盘从A移到C
        if cnt == m:
            print(f"#{num}: {source}->{target}")
        henoi(num - 1, auxiliary, source, target)  # 最后将B上的num-1个圆盘移到C上
    return cnt


n, m = map(int, input().split())
cnt = 0
print(henoi(n, 'A', 'B', 'C'))
