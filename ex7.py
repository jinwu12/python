#建立空字典
dict1={}
#为dict1赋值
#输出{0: 0, 1: 1, 2: 4, 3: 9}
dict1={x:x**2 for x in range(4)} 
print(dict1)
#增加一个元素，修改元素1的值
dict1[4]=16
dict1[1]='one'
#输出字典元素1和4的值:one 16
print(dict1[1],dict1[4])