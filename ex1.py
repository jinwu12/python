#数据类型转换
a,b,c=1,2.7,"jinwu"
d={}
print(type(a))
print(type(b))
print(type(c))
a=float(a)
b=int(b)
c1=tuple(c)
print(type(a),'\n',type(b),'\n',type(c1))
#推导式3
#计算20以内的奇数
d=[i for i in range(20) if i%2==1]
print(d)
#计算10以内奇数的平方数
d1={i:i**2 for i in d if i<10}
print(d1)
#元组推导式
c2=(i+'n' for i in c1)
print(tuple(c2))

