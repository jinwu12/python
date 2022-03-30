from peewee import *
from playhouse.shortcuts import model_to_dict
# 建立数据库链接
mydb = MySQLDatabase('test', host='localhost', user='root',
                     passwd='JXhbjzsb12')
mydb.connect

# 定义一个类model


class Symbol(Model):
    id = AutoField(primary_key=True)
    Symbol_name = CharField(max_length=256)
    comments = TextField()
    timezone = CharField(max_length=16)
    Symbol_value = CharField(max_length=256)
    contract_size = CharField(max_length=16)
    digits = IntegerField()
    threepoint_price = DoubleField(column_name="3point_price")
    Baseprice = DecimalField()

    class Meta:
        database = mydb
        table_name = "Symbol"

    # 初始化方法，表不存在就创建表，并插入一条记录
    def add(data):
        if not Symbol.table_exists():
            Symbol.create_table()
        Symbol.insert(data).execute()

    # 读取表中Symbol_name为“name”的数据
    def read(name):
        sy = Symbol.get(Symbol.Symbol_name == name)
        # 将sy转换成一个字典
        i = model_to_dict(sy)
        print(i)


'''
测试案例：data
结果：{'id': 10, 'Symbol_name': 'Char', 'comments': 'Text',
'timezone': 'Char', 'Symbol_value': 'Cha', 'contract_size': 'CharFiel',
'digits': 34, 'threepoint_price': 9978798.0, 'Baseprice': Decimal('4.00000')}

#########################
data = {'Symbol_name': 'Char',
        'comments': 'Text',
        'timezone': 'Char',
        'Symbol_value': 'Cha',
        'contract_size': 'CharFiel',
        'digits': 34,
        'threepoint_price': 9978798,
        'Baseprice': 4}
Symbol.add(data)
Symbol.read('Char')
'''


class Combination(Model):
    id = AutoField(primary_key=True)
    Combination_name = CharField(max_length=256)
    Combined_model = CharField(max_length=32)
    Combination_3price = IntegerField()
    trading_symbol = CharField(max_length=256)
    Symbol_list = CharField(max_length=256)
    comments = TextField()
    Baseprice = DecimalField()

    class Meta:
        database = mydb
        table_name = "Combination"

    # 初始化方法，表不存在就创建表，并插入一条记录
    def add(data):
        if not Combination.table_exists():
            Combination.create_table()
        Combination.insert(data).execute()

    # 读取表中Combination_name为“name”的数据
    def read(name):
        cb = Combination.get(Combination.Combination_name == name)
        # 将cb转换成一个字典
        i = model_to_dict(cb)
        print(i)
'''
测试案例及结果
{'id': 1, 'Combination_name': 'test', 'Combined_model': 'anyw', 
'Combination_3price': 67, 'trading_symbol': '', 'Symbol_list': '',
 'comments': 'TextField()', 'Baseprice': Decimal('7.23000')}
'''
data = {'Combination_name': 'test',
        'Combined_model': 'anyw',
        'Combination_3price': 67,
        'comments': 'TextField()',
        'Baseprice': 7.23}
Combination.add(data)
Combination.read('test')
