print('请开始你的猜数小游戏,猜的数字在1到20之间')
import random
ds = random.randint(1, 20)
count = 0
while True:
    num = int(input('请输入您猜的数'))
    count = count + 1
    if num == ds:
        print("恭喜您猜对了!")
        break
    else:
        if num > ds:
            print('您猜大了')
        else:
            print('您猜小了')
print(f'您猜了{count}次')
