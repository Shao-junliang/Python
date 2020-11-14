dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

""""
写法：字典序列[key] = 值
注意：如果key存在则修改这个key对应的值 ；如果key不存在则新增此键值对。
"""
# 修改
dict1['name'] = 'Lily'
print(dict1)

# 新增
dict1['id'] = 110
print(dict1)
