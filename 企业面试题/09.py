# 用Python代码实现Python内置函数max
l = [1, 2, 3, 4, 5, 6]
print(max(l))
print(max(2, 6, 5, 4))
l2 = [
    {'name': '张三', 'age': 20},
    {'name': '李四', 'age': 30},
    {'name': '王五', 'age': 40},
    {'name': '赵六', 'age': 50}
]

print(max(l2, key=lambda x: x['age']))


def my_max(*args, key=None):
    args = args [0] if len(args) == 1 else args
    if key == None:
        max_ = args[0]
        for n in args:
            if n > max_:
                max_ = n
        return max_
    else:
        max_ = args[0]
        for n in args:
            if key(n) > key(max_):
                max_ = n
        return max_
    
print(my_max([1, 2, 3, 4, 5, 6]))
print(my_max(1, 2, 3, 4, 5, 6))
print(my_max(l2, key=lambda x: x['age']))
    