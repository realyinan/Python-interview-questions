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

# 在 Python 中，默认参数在函数定义时只被计算一次。这意味着如果默认参数是一个可变对象（如列表、字典或其他对象），它在后续调用中会保持状态。


