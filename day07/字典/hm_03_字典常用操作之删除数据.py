dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

""""
del() / del：删除字典或删除字典中指定键值对。
clear()：清空字典
"""
# 删除指定键值对
del dict1['name']
print(dict1)

# 清空字典
dict1.clear()
print(dict1)

# 删除字典
del dict1  # 或者del(dict1)



