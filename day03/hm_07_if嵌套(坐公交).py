# 坐公交：有钱，可以坐；没钱，不能坐。坐上后：有空座，可以坐着；没空座，只能站着。

"""
步骤：
    1.准备数据
    2.进行判断
    3.进行输出
"""
money = 1
seat = 1

if money >= 1:
    print("有钱，可以坐公交")
    if seat >= 1:
        print("有空座，可以坐下")
    else:
        print("没空座，只能站着")
else:
    print("没钱，不能坐公交")




