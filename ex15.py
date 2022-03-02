#打开文件wenjian.txt
f=open("wenjian.txt",'r+')
#读取一行
print(f.readline())
#写入一个字符串
f.write('4.4444444')
#关闭文件
f.close()