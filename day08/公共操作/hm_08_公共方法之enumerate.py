"""
语法：enumerate(可遍历对象, start=0)
注意：start参数⽤来设置遍历数据的下标的起始值，默认为0。
结果：返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据
"""
list1 = ['a', 'b', 'c', 'd', 'e']

for i in enumerate(list1):
    print(i, end=' ')
print()
for index, char in enumerate(list1, start=1):
    print(f'下标是{index},对应的字符是{char}')

