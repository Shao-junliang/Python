"""
关键字参数：函数调⽤，通过“键=值”形式加以指定。可以让函数更加清晰、容易使⽤，同时也清除了参数的顺序需求。
注意：函数调⽤时，如果有位置参数时，位置参数必须在关键字参数的前⾯，但关键字参数之间不存在先后顺序。
"""


def user_info(name, age, gender):
    print(f'您的名字是{name}，您的年龄是{age}，您的性别是{gender}')


user_info('TOM', age=20, gender='男')
user_info('TOM', gender='男', age=20)
# user_info('TOM', '男', age=20)  报错了




