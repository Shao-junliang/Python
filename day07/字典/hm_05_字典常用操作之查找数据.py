dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

"""
1.key值查找
2.函数查找
    2.1 get()
    语法：字典序列.get(key, 默认值)
    注意：如果当前查找的key不存在则返回第⼆个参数(默认值)，如果省略第⼆个参数，则返回None。
    2.2 keys() 查找字典中所有的key，返回可迭代对象（可迭代对象：指的是可以用for循环遍历的对象）
    2.3 values() 查找字典中所有的value，返回可迭代对象
    2.4 items() 查找字典中所有的键值对，返回可迭代对象，对象里面的数据是元组，元组的数据1是字典的key，元组的数据2是字典key对应的值
"""
# 1.[key]
print(dict1['name'])

# 2.函数
# 2.1 get()
print(dict1.get('name'))
print(dict1.get('names'))
print(dict1.get('names', '所查不存在'))

# 2.2 keys()
print(dict1.keys())

# 2.3 values()
print(dict1.values())

# 2.4 items()
print(dict1.items())

