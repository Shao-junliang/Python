"""
创建集合使⽤ {} 或 set() ， 但是如果要创建空集合只能使⽤ set() ，因为 {} ⽤来创建空字典。
特点：
    1. 集合可以去掉重复数据；
    2. 集合数据是⽆序的，故不⽀持下标
"""
# 1.创建有数据的集合
s1 = {10, 20, 30, 40, 50}
print(s1)

s2 = {10, 30, 20, 10, 40, 20, 50}
print(s2)

s3 = set('abcdefg')
print(s3)

# 2. 创建空集合
s4 = set()
print(s4)
print(type(s4))







