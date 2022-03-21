import time
#获取当前时间戳
t=time.time()
print(t)
#将时间戳转换成格式化时间
print(time.ctime(t))
#将时间戳转换成时间元组
T=time.localtime(t)
print(T)
#自定义格式化时间
print(time.strftime("%Y年%m月%d日 %H点%M分",T))
#将时间元组转换成格式化时间
print(time.asctime(T))
#将一个格式化时间转化为时间元组
T1=time.strptime("2020 03 6", "%Y %m %d")
print(T1)
#将时间元组转换成时间戳
print(time.mktime(T1))
#输出指定月份的日历
import calendar
c=calendar.month(2020, 3)
print(c)