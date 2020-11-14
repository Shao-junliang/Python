# 可变与不可变的引用

# 1. 不可变
a = 1
b = a
print(id(a))
print(id(b))

# 2. 可变
aa = [10, 20]
bb = aa

print(id(aa))
print(id(bb))

aa.append(30)
print(aa)
print(id(aa))
print(id(bb))


