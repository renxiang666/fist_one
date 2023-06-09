# 全局变量,可在函数内外都可以使用的变量

a = 10


def show1():
    print(a)
    # 局部变量,只能在函数内使用的变量
    b = 20
    print(b)


def show2():
    print(a)
    # print(b)  此行报错   因为b的值在自定义函数show1内

def show3():
    print(a)

#调用函数
show1()  #10 20
show2()  #10
show3()  #10

print(a)
# print(b)  此行报错,因为b实在函数内,数据局部变量
