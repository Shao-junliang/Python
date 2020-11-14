name_list = ['Tom', 'Lily', 'Rose']

"""
需求：注册邮箱，用户输入一个账号名，判断这个账号名是否存在，如果存在，提示用户，否则提示可以注册。
"""
# 1.用户输入一个账号
name = input("请输入您的帐号名：")

# 2.判断是否重复
if name in name_list:
    print(f"您输入的名字是{name}，此用户名已经存在")
else:
    print(f"您输入的名字是{name}")



