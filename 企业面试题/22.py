# 说出下面代码的运行结果
def extend_list(val, items=[]):
    items.append(val)
    return items

list1 = extend_list(10)
list2 = extend_list(123, [2, 3])
list3 = extend_list('a')

print(list1)
print(list2)
print(list3)



