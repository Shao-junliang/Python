s1 = {10, 20, 30, 40, 50}

"""
1. remove()，删除集合中的指定数据，如果数据不存在则报错。
2. discard()，删除集合中的指定数据，如果数据不存在也不会报错。
3. pop()，随机删除集合中的某个数据，并返回这个数据。
"""
# 1. remove()
s1.remove(10)
print(s1)

# s1.remove(100)  # 数据不存在报错
# print(s1)

# 2. discard()
s1.discard(10)  # 数据不存在不报错
print(s1)

# 3. pop()
del_num = s1.pop()
print(del_num)
print(s1)