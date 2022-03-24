import pickle
# 输出格式美化
# 输出九九乘法表
j = 0
for i in range(1, 10):
    for j in range(1, i):
        print(repr(i*j).rjust(3), end=' ')
    print('{:3d}'.format(i*(j+1)))
# 读取输入
s = input("输入一个字符串：")
print(s)
# 文件和pickle模块
# 打开文件
f = open("wenjian.txt", 'ab+')
# 写入对象s
pickle.dump(s, f)
# 输出文件全部内容
f.seek(0)
print(f.read())
f.close()
