#堆栈应用
a=[1,2,3,4,5,6,7]
#增加一个元素
a.append(8)
#把元素依次从堆栈顶释放出来:8 7 6 5 4 3 2 1
x=0
i=len(a)
while x<i:
    print(a.pop())
    x+=1
#构造一个嵌套列表:[[1, 2], [3, 4], [5, 6]]
a=[1,2,3,4,5,6]
b=[[a[i+2*j] for i in range(2) ] for j in range(3)]
print(b)
#将2X3的矩阵列表转换为3X2列表:[[1, 3, 5], [2, 4, 6]]
b1=[[j[i] for j in b] for i in range(2)]
print(b1)
#队列应用
#依次输出队列中的元素
print(b1.pop(0))
print(b1.pop(0))