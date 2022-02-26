import random
#生成一个随机数a
a=random.random()
print(a)
'''
a大于0.9输出一等奖
a大于0.7小于0.9输出二等奖
a在0.4到0.7之间三等奖
a小于0.4输出擦肩而过
'''
if a>0.9:
    print('一等奖')
elif a>0.7:
    print('二等奖')
elif a>0.4:
    print("三等奖")
else:
    print('擦肩而过')