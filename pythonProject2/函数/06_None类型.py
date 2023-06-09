# 1.先定义函数
def get_avg(a, b):
    avg = (a + b) / 2
    print(avg)
    return avg  # 如果不写return,默认返回None


s = get_avg(100, 50)  # 调用函数
print(s)
