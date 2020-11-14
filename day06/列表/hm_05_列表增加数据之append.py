name_list = ['Tom', 'Lily', 'Rose']

"""
append()：列表结尾追加数据。
语法：列表序列.append(数据)
注意点：如果append()追加的数据是⼀个序列，则追加整个序列到列表
"""
name_list.append('xiaoming')
print(name_list)

name_list.append([11,22])
print(name_list)

"""
观察上述结果：
    1.列表是可变的，但是除了追加单个字符串，能否追加一个列表序列呢？
    2.append函数追加数据的时候如果数据是一个序列，追加整个序列到列表结尾。
"""
