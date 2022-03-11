#定义一个类
class two():
    a=1
    b=1
    #类的构造函数
    def __init__(self,a,b):
        self.a=a
        self.b=b
    #定义一个方法，输出两个数中更大的一个
    def max(self):
        if self.a>=self.b:
            print('最大数是',self.a)
        else:
            print('最大数是',self.b)
#实例化类，并调用类的方法            
m=two(5, 24)
m.max()
#类的继承
class three(two):
    def __init__(self,a,b,c):
        #调用父类的构造函数
        two.__init__(self, a, b)
        self.c=c
    #覆写父类的方法
    def max(self):
        if self.a<self.b:
            self.a=self.b
        if self.a<self.c:
            self.a=self.c
        print('最大数是',self.a)
#实例化子类
n=three(31, 76, 55)
n.max()

