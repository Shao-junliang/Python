age = int(input("请输入您的年龄："))

if age <= 18:
    print(f"您的年龄是{age}，属于童工。")

elif 18 <= age <= 60:
    print(f"您的年龄是{age}，合法工龄。")

else:
    print(f"您的年龄是{age}，可以退休。")