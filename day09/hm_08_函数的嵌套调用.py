# 两个函数 testA 和 testB --在A里面嵌套调用B


def testB():
    print('B函数开始')
    print('这是B函数')
    print('B函数结束')


def testA():
    print('A函数开始')
    testB()
    print('A函数结束')


testA()
