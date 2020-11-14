""""
需求：进⼊系统显示系统功能界⾯，功能如下：
    1. 添加学员
    2. 删除学员
    3. 修改学员信息
    4. 查询学员信息
    5. 显示所有学员信息
    6. 退出系统
    系统共6个功能，⽤户根据⾃⼰需求选取。
"""
"""
步骤分析：
    1. 显示功能界面
    2. 用户输入功能序号
    3. 根据用户输入的功能序号，执行不同功能（函数）
        3.1 定义函数
        3.2 调用函数
"""

info = []


# 系统功能需要循环使用，直到用户输入，才退出系统
while True:
    def print_info():
        print('请选择功能序号：')
        print('1. 添加学员')
        print('2. 删除学员')
        print('3. 修改学员信息')
        print('4. 查询学员信息')
        print('5. 显示所有学员信息')
        print('6. 退出系统')
        print('-' * 20)

    # 添加学员信息
    """
    添加学员：
        1. 接收用户输入信息，并保存
        2. 判断是否添加
            2.1 如果学员姓名已存在，报错提示
            2.2 如果不存在，则将用户输入的信息保存于一个空字典中，然后再将字典追加至列表中
        3. 对应的if条件成立的位置调用该函数
    """


    def add_info():
        """添加学员函数"""
        pass
        # 1. 保存学员信息
        new_name = input('请输入姓名：')
        new_id = input('请输入学号：')
        new_tel = input('请输入电话：')

        # 2. 判断是否存在
        global info  # 声明全局变量
        for i in info:
            if new_name == i['name']:
                print('该用户已存在！')
                return

        if new_name in info:
            pass
        else:
            pass

        dict1 = {}
        print('请输入学员信息：')
        dict1 = input()

        info.append(a)
    # 1. 显示功能界面
    print_info()
    # 2. 用户输入功能序号
    uesr_num = int(input('请输入序号：'))

    # 3. 按照用户输入的序号，执行不同功能

    if uesr_num == 1:
        # print('添加学员')
        add_info()
    elif uesr_num == 2:
        print('删除学员')
    elif uesr_num == 3:
        print('修改学员信息')
    elif uesr_num == 4:
        print('查询学员信息')
    elif uesr_num == 5:
        print('显示所有学员信息')
    elif uesr_num == 6:
        print('退出系统')
        break
    else:
        print('输入序号不正确，请重新输入')





