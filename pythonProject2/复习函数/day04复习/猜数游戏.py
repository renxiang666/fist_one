# 导入random生成随机底数
import random

ds = random.randint(1, 100)

print(f'后台查看底数为{ds}')

for i in range(3):
    num = int(input('请输入您猜的数'))
    if 1 <= num <= 100:
        if num == ds:
            print('恭喜您中奖了')
            break
        else:
            if num > ds:
                print('您猜大了')
            else:
                print('您猜小了')
    else:
        print('请查看好游戏规则')
