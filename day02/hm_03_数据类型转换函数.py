# 1.float()
num1 = 1
str1 = '10'
print(type(num1))
print(type(float(num1)))
print(float(num1))

print(type(str1))
print(type(float(str1)))
print(float(str1))
# 2.str()
print(type(str(num1)))

# 3.tuple() --将序列转换成元组
list1 = [10, 20, 30]

print(tuple(list1))
# 4.list() --将序列转换成列表
t1 = (100, 200, 300)
print(list(t1))

# 5.eval() --计算在字符串中的有效Python表达式，并返回一个对象。

# 即将字符串中的数据转换成他原本的类型
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'
print(eval(str2))
print(type(eval(str2)))
print(eval(str3))
print(type(eval(str3)))
print(eval(str4))
print(type(eval(str4)))
print(eval(str5))
print(type(eval(str5)))
#