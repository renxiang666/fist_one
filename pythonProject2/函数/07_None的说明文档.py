# 1.先定义函数
def get_avg(a, b):
    """
    :param a: 参数a是一个整数
    :param b: 参数b是一个整数
    :return: 返回值是平均数
    """
    avg = (a + b) / 2
    print(avg)
    return avg  # 如果不写return,默认返回None


s = get_avg(100, 50)  # 调用函数
print(s)

print('_____________________________')


def all_sum(a, b):  # 定义函数
    """

    :param a: 整数
    :param b: 整数
    :return: 和
    """
    sum = a + b
    return sum  # 设置返回值sum


sum = all_sum(100, 88)  # 定义函数
print(sum)

help(all_sum)