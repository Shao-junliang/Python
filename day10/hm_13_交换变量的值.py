# 交换a，b的值

# 1. 用第三方变量进行存储然后交换
a, b = 1, 2
print(a, end=' ')
print(b)
c = a
a = b
b = c
print(a, end=' ')
print(b)


# 2. 不用第三方变量
a, b = b, a
print(a, end=' ')
print(b)



