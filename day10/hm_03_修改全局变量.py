# 将全局变量改为200
"""
global 关键字声明a是全局变量
"""
a = 100


def testA():
    print(a)


def testB():
    global a
    a = 200
    print(a)


testA()
testB()
print(f'全局变量a={a}')
"""
函数体内部修改全局变量必须要用global先声明，在修改。
"""

