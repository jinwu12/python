import time
import threading
a = 0


# 输入变量a值的线程
class inthread(threading.Thread):

    # 构造线程ID和输入次数
    def __init__(self, threadID, i):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.i = i

    def run(self):
        # 全局变量a
        global a
        while self.i > 0:
            # 输入一个值给a，并输出线程ID和当前时间戳
            a = input('输入一个数：')
            self.i -= 1
            print(self.threadID, time.time())
            time.sleep(2)

        print('结束', self.threadID)


class outthread(threading.Thread):

    b = 0

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    # 检测30秒内a值的变动情况
    def run(self):
        global a
        i = 0
        j = 0
        while j < 30:
            if self.b == a:
                pass
            # a的值改变后输出a和变动次数
            else:
                print('a的值发生改变：', a)
                self.b = a
                i += 1
                print('第{}次改变，时间{}'.format(i, time.time()))
            # 每秒检测一次
            time.sleep(1)
            j += 1

        print('结束', self.threadID)


# 创建线程1和2
thread1 = inthread(1, 5)
thread2 = outthread(2)
# 开启线程:输入和结果
'''
输入一个数：2
1 1648181692.9087012
a的值发生改变： 2
第1次改变，时间1648181693.6757002
输入一个数：6
1 1648181699.6868863
a的值发生改变： 6
第2次改变，时间1648181700.6794298
输入一个数：6
1 1648181703.1961384
输入一个数：2
1 1648181706.7231839
a的值发生改变： 2
第3次改变，时间1648181707.6846614
输入一个数：5
1 1648181710.5553136
a的值发生改变： 5
第4次改变，时间1648181710.6873076
结束 1
结束 2
'''
thread1.start()
thread2.start()
