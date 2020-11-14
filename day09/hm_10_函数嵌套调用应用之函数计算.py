a = int(input())
b = int(input())
c = int(input())


def sum_sum(d, e, f):
    return a + b + c


def average_sum(d, e, f):
    sumResult = sum_sum(d, e, f)
    return sumResult / 3


print(average_sum(a, b, c))

