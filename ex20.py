#定义全局变量a
a=1
def test1():
    #改变局部变量a的值
    b=2
    a=b
    print(a)
#局部变量值的改变不会影响全局变量，结果2，1
test1()
print(a)
def test2():
    #声明全局变量a
    global a
    b=2
    a=b
    print(a)
#全局变量a的值被改变，结果：2，2
test2()
print(a)