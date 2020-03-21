#冒泡排序（从小到大）
list = [23,67,11,89,333,666,234]

for i in range(0,len(list)-1):                  #外层循环控制比较轮数
    for j in range(0,len(list)-1-i):            #内层循环控制每轮比较的次数
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
print(list)

