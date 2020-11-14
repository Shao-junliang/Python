mystr = "hello world and itcast and itheima and Python"

"""
capitalize()：将字符串第⼀个字符转换成⼤写。
注意：capitalize()函数转换后，只字符串第⼀个字符⼤写，其他的字符全都⼩写。
"""
new_str = mystr.capitalize()
print(new_str)

"""
title()：将字符串每个单词⾸字⺟转换成⼤写。
"""
new_str1 = mystr.title()
print(new_str1)

"""
lower()：将字符串中⼤写转⼩写。
"""
new_str2 = mystr.lower()
print(new_str2)

"""
upper()：将字符串中⼩写转⼤写。
"""
new_str3 = mystr.upper()
print(new_str3)


mystr1 = "   hello world and itcast and itheima and Python   "
"""
lstrip()：删除字符串左侧空⽩字符。
"""
new_str4 = mystr1.lstrip()
print(new_str4)

"""
rstrip()：删除字符串右侧空⽩字符。
"""
new_str5 = mystr1.rstrip()
print(new_str5)

"""
strip()：删除字符串两侧空⽩字符。
"""
new_str6 = mystr1.strip()
print(new_str6)

mystr2 = 'hello'

"""
ljust()：返回⼀个原字符串左对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串。
rjust()：返回⼀个原字符串右对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串，语法和ljust()相同。
center()：返回⼀个原字符串居中对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串，语法和ljust()相同。
语法：字符串序列.ljust(⻓度, 填充字符)
"""
new_str7 = mystr2.ljust(10)
new_str8 = mystr2.ljust(10, '.')
print(new_str7)
print(new_str8)

new_str9 = mystr2.rjust(10)
new_str10 = mystr2.rjust(10, '.')
print(new_str9)
print(new_str10)

new_str11 = mystr2.center(10)
new_str12 = mystr2.center(10, '.')
print(new_str11)
print(new_str12)
