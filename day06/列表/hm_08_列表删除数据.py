name_list = ['Tom', 'Lily', 'Rose']

"""
1.del 删除列表
语法：del ⽬标 or del(目标)
注意：del还可以删除指定下标的数据
eg：del(name_list[0])
"""
# del name_list

"""
2.pop()：删除指定下标的数据(如果不指定下标数据，默认为最后⼀个)，并返回这个被删除的数据。
"""
del_name = name_list.pop(1)
print(del_name)
print(name_list)
del_name = name_list.pop()
print(name_list)

"""
3.remove()：移除列表中某个数据的第⼀个匹配项。
语法：列表序列.remove(数据)
"""
name_list1 = ['Tom', 'Lily', 'Rose', 'Rose']
name_list1.remove('Rose')
print(name_list1)

"""
4. clear()：清空列表
"""
name_list1.clear()
print(name_list1)
del name_list1

