import mysql.connector
#建立数据库连接
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="JXhbjzsb12"   # 数据库密码
)
#建立一个数据库操作用的链接？
caozuo=mydb.cursor()
#建立test数据库
#caozuo.execute("CREATE DATABASE test")
#显示数据库
caozuo.execute("SHOW DATABASES")
for x in caozuo:
  print(x)
#进入test库
caozuo.execute('USE test')
#建立表
caozuo.execute('CREATE TABLE people (ID VARCHAR(255), name VARCHAR(255))')
#显示表
caozuo.execute("SHOW TABLES")
for x in caozuo:
  print(x)