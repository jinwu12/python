import time
import datetime
import pytz
# 获取当前时间戳
t = 1580616000
#时间戳格式化输出
print(time.strftime("%Y-%m-%d",time.localtime(t)))
# 将时间戳转换成格式化时间
print(time.ctime(t))
#将时间戳转换成datetime对象
T=datetime.datetime.fromtimestamp(t)
#datetime对象转换时间戳
print(T.timestamp())
#时区转换或datetime.datetime.fromtimestamp(time, tz)
tz=pytz.timezone('Etc/GMT+5')
T=T.replace().astimezone(tz)
print(T.strftime("%Y-%m-%d"))
#datetime分拆及合成
T=datetime.datetime.combine(T.date(), datetime.time(22,0,0,0))
print(T)
#datetime对象转换时间元组
print(T.timetuple())

#自定义格式化时间
#print(time.strftime("%Y年%m月%d日 %H点%M分",T))
'''
#将时间元组转换成格式化时间
print(time.asctime(T))
#将一个格式化时间转化为时间元组
T1 = time.strptime("2020 03 6", "%Y %m %d")
print(T1)
#将时间元组转换成时间戳
print(time.mktime(T1))
#输出指定月份的日历p
import calendar
c=calendar.month(2020, 3)
print(c)
'''