# 需求：有三个办公室，8位⽼师，8位⽼师随机分配到3个办公室
"""
步骤：
1.准备数据
    1.1八位老师数据（名字）--列表
    1.2三个办公室数据（名字）--列表（嵌套3个）
2.分配老师到办公室
    ***随机分配（重点）
    就是把老师的名字写入到办公室列表 -- 办公室列表追加老师名字
3.验证是否分配成功
    打印办公室详细信息
"""
import  random

# 1.准备数据
teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
offices = [[], [], []]

# 2.随机分配
for name in teachers:
    # 列表追加数据 -- append(选中) extend insert
    # 不能指定是具体某个下标 -- 随机
    num = random.randint(0, 2)
    offices[num].append(name)

# print(offices)

# 为了更贴合生活，把各个办公室子列表进行编号：1，2，3
i = 1
# 3.验证是否分配成功
for office in offices:
    # 打印办公室人数
    print(f"办公室{i}的人数是{len(office)}，老师分别是：")
    # 打印老师的名字 -- 每个子列表里面的名字不一样 -- 遍历 -- 子列表
    for name in office:
        print(name, end=' ')
    print()
    i += 1

