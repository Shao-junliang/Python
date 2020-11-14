t1 = ('aa', 'bb', 'cc', 'bb')
print(t1[0])

"""
index()：查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index⽅法相同。
count()：统计某个数据在当前元组出现的次数。
len()：统计元组中数据的个数。
"""
print(t1.index('bb'))
print(t1.count('bb'))
print(len(t1))



