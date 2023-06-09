name_list = ['张三', '李四', '王五', '赵六']
print(name_list)

name_list[0] = '熊大'
print(name_list)

name_list[1] = '熊二'
print(name_list)

name1 = name_list[0]
print(name1)

count1 = name_list.count('王五')
print(count1)

count2 = name_list.count('王九')
print(count2)

index = name_list.index('赵六')
print(index)

ll = len(name_list)
print(ll)
