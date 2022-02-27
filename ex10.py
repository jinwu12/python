#使用for循环为列表赋值：1至19
list1=[x for x in range(1,20)]
print(list1)
#输出list13的倍数,遇到9跳过，遇到13终止循环:3 6 12
x=-1
while x<19:
    x+=1
    if list1[x]==9:
        continue
    elif list1[x]==13:
        break
    if list1[x]%3==0:
        print(list1[x],end=" ")