# 需求：一个函数要返回两个数1、2
"""
遇到return退出函数。
"""


def return_num():
    return 1, 2, 'a'


result = return_num()
print(result)  # 返回的值为一个元组
print(return_num())
"""
结论：return后面可以直接书写元组、列表、字典，返回多个值
"""



