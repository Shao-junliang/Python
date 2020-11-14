glo_num = 0  # 定义一个全局变量


def test1():
    global glo_num
    glo_num = 100
    print(glo_num)


def test2():
    print(glo_num)


print(glo_num)
test1()
test2()
print(glo_num)









