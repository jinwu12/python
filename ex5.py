list1=[10,20,30,40,50]
list2=[70,80,90]
#增加元素60
list1.append(60)
#输出[10,20,30,40,50,60]
print(list1)
#连接list1和list2
list1+=list2
#输出[10,20,30,40,50,60,70,80,90]
print(list1)
#删除最后一个元素
del list1[-1]
#输出[10,20,30,40,50,60,70,80]
print(list1)
#输出元素个数，最大元素，最小元素：8 80 10
print(len(list1),max(list1),min(list1))
#30在list1中出现的次数：1
print(list.count(list1, 30))