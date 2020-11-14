# help函数：用来查看函数的说明文档
# help(len)

"""
def 函数名(参数):
"""
# 说明⽂档的位置
"""
    代码
    ......
注意：必须在函数内部第一行书写的才是说明文档，然后使用help可以调出说明文档
"""


def sum_sum(a, b):
    """求和函数"""
    return a + b


help(sum_sum)

"""
函数说明文档的高级使用
"""


def sum_sum1(a, b):
    """
    求和函数
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    return a + b


help(sum_sum1)


