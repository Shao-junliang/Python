"""
1. tuple(): 将某个序列转换成元组
2. list(): 将某个序列转换成列表
3. set(): 将某个序列转换成集合
"""

list1 = [10, 20, 30, 20, 40, 50]
s1 = {100, 300, 200, 500}
t1 = {'a', 'b', 'c', 'd', 'e'}

# tuple(): 将某个序列转换成元组
print(tuple(list1))
print(tuple(s1))

# list(): 将某个序列转换成列表
print(list(s1))
print(list(t1))

# set(): 将某个序列转换成集合
print(set(list1))
print(set(t1))

