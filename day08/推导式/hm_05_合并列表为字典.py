"""
作用：快速合并列表为字典或提取字典中⽬标数据。
"""
# 需求：将两个列表合并为字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', '18', 'man']

dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)

list1 = ['name', 'age', 'gender', 'id']
list2 = ['Tom', '18', 'man']

dict1 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict1)

"""
结论：
    1. 如果两个列表数据个数相同，len统计任何一个列表的长度都可以。
    2. 如果两个列表数据长度不同，len统计数据少的列表不会报错，统计数据多的列表会报错。
"""

