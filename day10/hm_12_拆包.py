# 1. 拆包元组数据


def return_num():
    return 100, 200


tuple1 = return_num()
print(tuple1)
print(type(tuple1))
# 拆包
num1, num2 = return_num()
print(num1)
print(num2)

# 2. 拆包字典数据
dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1
# 对字典进行拆包，取出来的是字典的key
print(a)
print(b)

print(dict1[a])
print(dict1[b])



