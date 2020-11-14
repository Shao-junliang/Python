name_list = ['Tom', 'Lily', 'Rose']

# 1.修改指定下标的数据
name_list[0] = 'xiaoming'
print(name_list)

# 2.逆置：reverse()
list1 = [1, 3, 2, 5, 4, 6]
list1.reverse()
print(list1)

"""
3.排序：sort()
语法：1 列表序列.sort( key=None, reverse=False)
key 是如果未来用到的列表中有字典，要按照字典的某个key值排序时，会用到key。
注意：reverse表示排序规则，reverse = True 降序， reverse = False 升序（如果不写默认为升序）
"""
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)





