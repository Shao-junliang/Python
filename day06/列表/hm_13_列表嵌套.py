name_list = [['小明', '小红', '小刚'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]

print(name_list)

# 嵌套列表的数据查询
print(name_list[2][1])

for i in name_list:
    for j in i:
        print(j, end=' ')
    print()
