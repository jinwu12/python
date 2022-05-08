import math
a=4
b=-1.21
c=0x10
d=complex(5,9)
#4,-1.21,16,5+9j
print(a,b,c,d)
#1.21,-2,2
e1=abs(b)
e2=math.floor(b)
e3=math.log(c,a)
print(e1,e2,e3)
import os
#os.makedirs('assist/set')
os.path.exists('assist')