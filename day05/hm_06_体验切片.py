# 语法：序列[开始位置下标:结束位置下标:步⻓]

name = '012345678'

print('---------------步长测试---------------')

print(name[0:2:1])
print(name[0:2:])
print(name[0:2])

print('---------------开始结尾测试---------------')

print(name[0:6:2])
print(name[:6:2])  # 不写开始，默认从0开始
print(name[0::2])  # 不写结束，表示选取到最后
print(name[::2])  # 不写开始和结束，表示选取所有

print('--------------负数测试----------------')

# 步长为负数 负数为倒序
print(name[::-1])
print(name[-4:-1])

print('--------------终极测试----------------')
print(name[-4:-1:1])
print(name[-1:-4:-1])
print(name[-4:-1:-1])  # 不能选取出数据

# 结论：如果选取方向（下标开始到结束的方向）和步长的方向冲突，则无法选取数据

