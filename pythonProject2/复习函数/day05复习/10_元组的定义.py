tuple1 = ()
print(tuple1)

tuple2 = tuple()
print(tuple2)

name1 = '张三'
print(name1, type(name1))

tuple3 = ('张三')
print(tuple3, type(tuple3))

name_tuple = ('张三', '李四', '王五', '赵六')
print(name_tuple, type(name_tuple))

# 特殊情况元组嵌套
name_tuple1 = ('张三', '李四', '王五', '赵六')
age_tuple1 = (18, 28, 38, 48)
student_tuple = (name_tuple1, age_tuple1)
print(student_tuple)
