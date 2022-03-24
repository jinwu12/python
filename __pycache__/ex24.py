import time
class timezone():
    #获取原始时区
    now_tz=int(time.timezone/3600)
    new_t=0
    def __init__(self,t,tz):
        #获取原始时间
        self.t=t
        #获取目标时区
        self.tz=tz
    def cgtz(self):
        #原始时间转换成目标时间并按要求输出
        self.new_t=self.t-(self.tz-self.now_tz)*3600
        print('原始时间：{},原始时区：{}'.format(time.ctime(self.t),self.now_tz))
        print('目标时间：{},目标时区：{}'.format(time.ctime(self.new_t),self.tz))
class tz1(timezone):
    #重写方法，增加原始和目标时间的时间戳
    def cgtz(self):
        timezone.cgtz(self)
        print('原始时间戳：{},目标时间戳：{}'.format(self.t,self.new_t))
class tz2(timezone):
    #重写方法，增加UTC0时区的时间和时间戳
    def cgtz(self):
        timezone.cgtz(self)
        print('UTC0时间戳：{},UTC：{}'.format(time.mktime(time.gmtime(self.t)),0))
t=time.time()
#调用父类
'''
原始时间：Thu Mar 24 14:52:31 2022,原始时区：-8
目标时间：Thu Mar 24 11:52:31 2022,目标时区：-5
'''
change=timezone(t, -5)
change.cgtz()
#调用子类1
'''
原始时间：Thu Mar 24 14:52:31 2022,原始时区：-8
目标时间：Thu Mar 24 04:52:31 2022,目标时区：2
原始时间戳：1648104751.5234015,目标时间戳：1648068751.5234015
'''
change1=tz1(t,2)
change1.cgtz()
#调用子类2
'''
原始时间：Thu Mar 24 14:52:31 2022,原始时区：-8
目标时间：Thu Mar 24 06:52:31 2022,目标时区：0
UTC0时间戳：1648075951.0,UTC：0
'''
change3=tz2(t, 0)
change3.cgtz()