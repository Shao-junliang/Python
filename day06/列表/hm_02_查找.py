name_list = ['Tom', 'Lily', 'Rose']

# 1.index()：返回指定数据所在位置的下标 。
"""
语法：列表序列.index(数据, 开始位置下标, 结束位置下标)
注意：如果查找的数据不存在则报错。
"""
print(name_list.index('Tom'))
# print(name_list.index('Toms'))

# 2.count()：统计指定数据在当前列表中出现的次数。
print(name_list.count('Tom'))
# print(name_list.count('Toms'))

# 3.len()：访问列表⻓度，即列表中数据的个数。
print(len(name_list))



