# 定义一个错误类
class MYError(Exception):
    pass


d = [5, 'a', 0, 16]
# 10分别除以d的各元素
for i in d:
    try:
        # 如果i大于10或者小于0，抛出自定义错误类
        if i > 10 or i < 0:
            raise MYError
        a = 10/i
    # 自定义错误
    except MYError:
        print('数值超出范围')
# 除数类型错误
    except TypeError:
        print("{}不是数字".format(i))
# 除数是0
    except ZeroDivisionError:
        print('0不能作除数')
# 计算没有异常
    else:
        print('10除以{0}的结果是{1}'.format(i, a))
# 完成一次try语句
    finally:
        print('完成一次计算')
# 循环结束
print('全部完成')
