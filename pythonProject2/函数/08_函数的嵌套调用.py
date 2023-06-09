# 函数的嵌套调用
def show2():
    print('2222222222')
    print('很多代码')
    print("2222222222")


def show0():
    print('000000000000000')
    show2()
    print("0000000000000000")


show0()
