a = input("请输入一个值：")  # 这里定义了全局变量 a

def print_a():
    print(a)  # 在函数内部直接调用全局变量 a

print_a()