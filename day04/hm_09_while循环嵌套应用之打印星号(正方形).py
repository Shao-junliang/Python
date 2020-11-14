"""
1.打印一个*
2.一行打印五个：内循环
3.打印五行，外循环
"""

i = 0
while i < 5:
    j = 0
    while j < 5:
        print("*", end="")
        j += 1
    print()
    i += 1
