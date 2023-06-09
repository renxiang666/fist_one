name_tuple = ('张三', '李四', '王五', '赵六')
print(name_tuple)

name = name_tuple[0]
print('第一个元素值', name)

name = name_tuple[-1]
print('最后一个元素值', name)

count = name_tuple.count('王五')
print('王五的个数', count)

index = name_tuple.index('赵六')
print('赵六的索引位置', index)

ll = len(name_tuple)
print('元素的个数', ll)
