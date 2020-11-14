"""
创建一个如下的列表：
    [(1, 0), (1, 1), (1, 2), (2, 0),(2, 1), (2, 2)]
"""

# 1.  while循环实现
list1 = []
i = 1
while i <= 2:
    j = 0
    while j < 3:
        list1.append((i, j))
        j += 1
    i += 1
print(list1)

# 2. for循环实现
list2 = []
for i in range(1, 3, 1):
    for j in range(3):
        list2.append((i, j))
print(list2)

# 3. 列表推导式实现
list3 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list3)

"""
结论：多for的列表推导式等同于for循环嵌套
"""

