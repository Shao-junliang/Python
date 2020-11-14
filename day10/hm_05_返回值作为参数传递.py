def test1():
    return 50


def test2(num):
    print(num)


result = test1()
test2(result)
test2(test1())


