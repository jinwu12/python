# 打开一个文件
f = open("wenjian.txt", 'r+')
# 逐行输出文件
for line in f:
    print(line)
f.close()
