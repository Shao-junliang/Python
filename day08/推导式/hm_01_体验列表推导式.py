"""
作用：用一个表达式创建一个有规律的列表或控制一个有规律列表(可以化简代码)
"""
# 需求：创建一个0-10的列表。

# 1. while循环实现
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# 2. for循环实现
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 3. 列表推导式实现
list3 = [i for i in range(10)]
print(list3)