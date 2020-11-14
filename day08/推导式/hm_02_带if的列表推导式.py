# 需求：创建一个0-10的偶数列表。

# 1. range步长事先
list1 = [i for i in range(0, 10, 2)]
print(list1)

# 2. if加for循环实现
list2 = [i for i in range(10) if i % 2 == 0]
print(list2)