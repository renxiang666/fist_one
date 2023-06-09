# 导入random包,生成随机底数
import random

count = 0
ds = random.randint(1, 100)  # 随机生成1到100的底数
print(f'底数为{ds}')  # 查看生成第底数为
for i in range(3):
    num = int(input(f'请输入您猜的数'))
    count = count + 1  # 每次猜count都要加1
    if 1 <= num <= 100:
        if num == ds:
            print('中奖了')
            break
        else:
            if num > ds:
                print('您猜大了')
            else:
                print('您猜小了')
            if count==3:
                print('您今日的次数已经用完,明日再来')
            else:
                print(f'您还剩下{3-count}几次会')
    else:
        print('请注意查看好游戏规则')
