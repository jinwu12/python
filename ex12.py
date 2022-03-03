#!/usr/bin/python3
# Filename: ex12.py

#定义一个求最大公约数的函数
def gys(a,b):
    g=min(a, b)
    while g>0:
        if a%g==0 and b%g==0:
            return g
        else: g-=1
#调用函数gys（）：输出31
print(gys(155, 62))