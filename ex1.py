#数据类型转换
'''
int
float
str
'''
a,b,c=1,2.7,"jinwu"
print(type(a))
print(type(b))
print(type(c))
a=float(a)
b=int(b)
c1=tuple(c)
#float int tuple
print(type(a),type(b),type(c1))
#推导式
#计算20以内的奇数 
#[1,3,5,7,9,11,13,15,17,19]
d=[i for i in range(20) if i%2==1]
print(d)
#计算10以内奇数的平方数
#{1:1,3:9,5:25,7:49,9:81}
d1={i:i**2 for i in d if i<10}
print(d1)
#元组推导式
#jn,in,nn,wn,un
c2=(i+'n' for i in c1)
print(tuple(c2))