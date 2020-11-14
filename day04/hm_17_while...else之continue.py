"""
while 条件：
    条件成立重复执行的代码
else：
    循环正常结束之后要执行的代码
"""

i = 1
while i <= 5:
    if i == 3:
        print("这一遍不真诚,但可以容忍")
        i += 1
        continue
    print("媳妇儿，我错了")
    i += 1
else:
    print("媳妇儿原谅我了")



