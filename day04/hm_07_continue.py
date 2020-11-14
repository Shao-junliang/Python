# continue: 当条件成立，退出当前循环，继续执行下一次循环。

# 吃苹果
i = 1
while i <= 5:
    if i == 3:
        print("吃出了一个大虫子，这个苹果不吃了")
        # 注意：如果使用continue，在continue之前一定要修改计数器，否则进入死循环。
        i += 1
        continue
    print(f"吃了第{i}个苹果")
    i += 1









