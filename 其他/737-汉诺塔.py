def henoi(n: int, source, auxiliary, target):
    global cnt
    if n == 1:  # 终止条件
        cnt += 1
        return

    henoi(n - 1, source, target, auxiliary)  # ①将上面的n-1个盘子从A移动到B
    cnt += 1  # ②将第n个盘子移动到C
    henoi(n - 1, auxiliary, source, target)  # ③将B的n-1个盘子移动到C
    return cnt


cnt = 0
print(henoi(25, 'A', 'B', 'C'))
