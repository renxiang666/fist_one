import random

ds = random.randint(1, 100)
print(f'产生的底数为{ds}')
while True:
    num = int(input('请输入您猜的数'))
    if num == ds:
        print('恭喜您中奖了')
        break
    else:
        if num > ds:
            print('您猜大了')
        else:
            print('您猜小了')
