name_tuple = ('张三', '李四', '王五', '赵六')
print(name_tuple)

i=0
while i<=len(name_tuple)-1:
    elment=name_tuple[i]
    print(elment)
    i+=1
print('-----------------------------')

for elment in name_tuple:
    print(elment)