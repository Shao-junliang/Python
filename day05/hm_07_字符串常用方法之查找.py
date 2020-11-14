# 开始和结束位置下标可以省略，表示在整个字符串序列中查找。

mystr = "hello world and itcast and itheima and Python"

print('---------------------find---------------------')

# 1.find()
"""
find()：检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则返回-1。
语法：字符串序列.find(⼦串, 开始位置下标, 结束位置下标)
rfind()： 和find()功能相同，但查找⽅向为右侧开始。
"""

print(mystr.find('and'))  # 没有开始查找位置和结束查找位置，默认从头开始，查找到第一个就结束。
print(mystr.find('and', 15, 30))
print(mystr.find('ands', 15, 30))  # 'ands' 不存在，返回-1

print('---------------------index---------------------')

# 2.index()
"""
index()：检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则报异常。
语法：字符串序列.index(⼦串, 开始位置下标, 结束位置下标)
rindex()：和index()功能相同，但查找⽅向为右侧开始。
"""
print(mystr.index('and'))
print(mystr.index('and', 15, 30))
# print(mystr.index('ands', 15, 30))

print('-------------------count-----------------------')

# 3.count()
"""
count()：返回某个⼦串在字符串中出现的次数
语法：字符串序列.count(⼦串, 开始位置下标, 结束位置下标)
"""
print(mystr.count('and'))
print(mystr.count('ands'))

print('---------------------rfind---------------------')

# 4.rfind()
print(mystr.rfind('and'))
print(mystr.rfind('ands'))

print('---------------------rindex---------------------')

# 5.rindex()
print(mystr.rindex('and'))
# print(mystr.rindex('ands'))



