str1='www.runoob.com'
#生成一个迭代器
a=iter(str1)
#迭代器是一个内存地址
print(a)
#迭代器的遍历
for x in a:
    print(x,end=',')
#迭代完成标志StopIteration
try:
        print (next(a))
except StopIteration:
        print('遍历结束')