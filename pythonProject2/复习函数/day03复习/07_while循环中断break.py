i = 18
while True:
    if 70 > i >= 18:
        print(f"小伙子您现在{i}岁未到退休年龄,继续加油")
        i = i + 1
    else:
        i = 65
        print(f'您已{i}岁到达退休年龄')
        break
