import re
s = 'Ryan is 6 years old,66 is 2 years old'
# 从起始位置匹配，输出none
print(re.match('[0-9]+', s))
# 返回整个字符串的第一个匹配位置：（8，9）
r = re.search('[0-9]+', s)
print(r)
# 获取匹配的字符串：6
print(r.group())
# 匹配所有满足的字符串：【6，66，2】
print(re.findall('[0-9]+', s))
# 替换字符串中的单词为‘：’，结果：6：66：2：
r = re.sub(r'\D+', '：', s)
print(r)
# 建立一个正则表达式并找出人名和对应的年龄
P = re.compile(r'(\w+?) is (\d+)')
r = P.finditer(s)
# 迭代输出所有子串：Ryan 6，66 6
for i in r:
    print(i.group(1), i.group(2))
