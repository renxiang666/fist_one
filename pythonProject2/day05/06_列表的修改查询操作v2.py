name_list = ['张三', '李四', '王五', '赵六']
print(name_list)

name_list[0] = '熊大'
print(name_list)

name_list[1] = '熊大'
print(name_list)

name = name_list[0]
print('第一个元素的值', name)

count = name_list.count('王五')
print('王五的次数', count)

# index=name.index('赵六')
# print('"赵六的索引为:', index)   #错误,因为不存在赵六

ll = len(name_list)
print('整个列表中元素的个数为:', ll)
