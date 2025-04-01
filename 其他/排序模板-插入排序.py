def insertion_sort(n: int, lst: list[int]) -> list[int]:
    """
    插入排序模板
    :param n: 待排序的元素个数
    :param lst: 待排序的元素列表
    :return: 排序后的列表
    """
    for i in range(1, n):  # 从第二个元素开始
        key = lst[i]  # 选出当前要插入的元素
        j = i - 1  # 初始化指针指到需要插入的元素的位置的前一个位置
        while j >= 0 and lst[j] > key:  # 向前查找插入位置
            lst[j + 1] = lst[j]  # 指针所指元素向后移动
            j -= 1  # 指针往前移动
        lst[j + 1] = key  # 找到插入位置，插入元素key
    return lst


num = int(input())  # 待排序的元素个数
arr = list(map(int, input().split()))  # 待排序的元素列表
ans = insertion_sort(num, arr)
print(*ans)
