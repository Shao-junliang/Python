mystr = "hello world and itcast and itheima and Python"

print('---------------------替换---------------------')
# replace()
"""
语法：字符串序列.replace(旧⼦串, 新⼦串, 替换次数)
注意：替换次数如果查出⼦串出现次数，则替换次数为该⼦串出现次数。
重点：repla() 返回一个新字符串
"""
new_str = mystr.replace('and', 'he')
new_str1 = mystr.replace('and', 'he', 1)

print(new_str)
print(mystr.replace('and', 'he'))
print(new_str1)

new_str1 = mystr.replace('and', 'he', 10)
print(new_str1)

print('---------------------分割---------------------')

"""
split()：按照指定字符分割字符串。
语法：字符串序列.split(分割字符, num)
注意：num表示的是分割字符出现的次数，即将来返回数据个数为num+1个。
重点：split() 返回一个列表，并丢失分割字符，分割几次丢失几次。
"""
list1 = mystr.split('and')
print(list1)
list2 = mystr.split('and', 2)
print(list2)

print('---------------------合并---------------------')

"""
join()：⽤⼀个字符或⼦串合并字符串，即是将多个字符串合并为⼀个新的字符串。
语法：字符或⼦串.join(多字符串组成的序列)
"""
# 与上述mystr无关了。
mylist = ['aa', 'bb', 'cc']

# aa...bb...cc
new_str2 = "...".join(mylist)
print(new_str2)











