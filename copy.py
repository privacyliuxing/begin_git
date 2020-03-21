import copy
list = [1,2,3,"q","abc",[4,5,6],(7,8,9)]

#引用拷贝  只是给对象赋予了一个变量名
list1 = list
# list[2] = 0
# list[3] = "w"
# list[5][0] = 111

#浅拷贝
list2 = list.copy()
list[2] = 100
list[5][2] = 666
list.append(999)

#深拷贝
# list3 = list.deepcopy()
# list[2] = 100
# list[5][2] = 666

print(id(list))
print(id(list1))
print(id(list2))
print(list)
print(list1)
print(list2)
# print(list3)