name_list = []
print(name_list)

name_list.append('张三')
print(name_list)

name_list.extend(['张三1', '李四', '王五]'])
print(name_list)

name_list.insert(0, '张三2')
print(name_list)

name_list.pop(0)
print(name_list)

del name_list[-1]
print(name_list)

name_list.remove('张三1')
print(name_list)

name_list.clear()
print(name_list)
