"""
1.准备数据
2.格式化输出数据
"""

age = 22
name = 'TOM'
weight = 65.5
student = 1

# 1.今年我的年龄是x岁
print("今年我的年龄是%d岁" % age)

# 2.我的名字是x
print("我的名字是%s" % name)

# 3，我的体重是x公斤
print("我的体重是%f公斤" % weight)
print("我的体重是%.1f公斤" % weight)
"""
%f 默认保留6位小数
%.nf 就是保留n位小数。
"""

# 4.我的学号是x
print("我的学号是%d" % student)
print("我的学号是%03d" % student)
"""
%0nd 表示输出的整数显示n位数，不⾜以0补全，超出当前位数则原样输出
"""

# 5.我的名字是x，今年x岁了
print("我的名字是%s,今年%d岁了" % (name, age))
print("我的名字是%s,明年%d岁了" % (name, age+1))

# 6.我的名字是x，今年x岁了.体重x公斤.学号是x
print("我的名字是%s,今年%d岁了,体重%.1f公斤,学号是%03d" % (name, age, weight, student))





