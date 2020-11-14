name_list = ['Tom', 'Lily', 'Rose']

"""
extend()：列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表。
语法：列表序列.extend(数据)
"""
# name_list.extend('xiaoming')  # 会把字符串逐一追加到序列中，不适合

name_list.extend(['xiaoming', 'xiaohong'])
print(name_list)


