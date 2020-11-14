mystr = "hello world and itcast and itheima and Python"

"""
startswith()：检查字符串是否是以指定⼦串开头，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。
语法：字符串序列.startswith(⼦串, 开始位置下标, 结束位置下标)
"""
print(mystr.startswith("hello"))
print(mystr.startswith("hel"))
print(mystr.startswith("hello", 5, 20))

"""
endswith()：：检查字符串是否是以指定⼦串结尾，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。
语法：字符串序列.endswith(⼦串, 开始位置下标, 结束位置下标)
"""
print(mystr.endswith("Python"))
print(mystr.endswith("hon"))
print(mystr.endswith("Python", 5, 20))

"""
isalpha()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟则返回 True, 否则返回 False。
isdigit()：如果字符串只包含数字则返回 True 否则返回 False。
isalnum()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟或数字则返 回 True,否则返回False。
isspace()：如果字符串中只包含空⽩，则返回 True，否则返回 False。
"""
print(mystr.isalpha())
print(mystr.isdigit())
print(mystr.isalnum())
print(mystr.isspace())

mystr1 = 'hello'
mystr2 = '2148452'
mystr3 = 'hello5487451'
mystr4 = "        "

print(mystr1.isalpha())
print(mystr2.isdigit())
print(mystr1.isalnum())
print(mystr2.isalnum())
print(mystr3.isalnum())
print(mystr4.isspace())

