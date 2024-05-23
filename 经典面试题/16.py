# 请说说你对Python中高阶函数的认识

# 高阶函数

# map
l1 = [2, 3, 4, 5]
print(list(map(lambda x: x**2, l1)))
print(list(map(lambda x, y: x*y, [1, 2, 3], [4, 5, 6])))
print('*'*80)

# reduce: 累计运算
from functools import reduce
print(reduce(lambda a, b: a+b, [2, 3, 4, 5]))
print('*'*80)

# sorted: 排序
l2 = [2, 1, 6, 3, 5, 9, 0]
print(sorted(l2))

l3 = [
    {'name': 'zhangsan', 'age': 33},
    {'name': 'zhangsi', 'age': 22},
    {'name': 'zhangwu', 'age': 44},
    {'name': 'wangwu', 'age': 14},
]
print(sorted(l3, key=lambda b: b['age'], reverse=True))
print('*'*80)

# filter:过滤
l4 = [2, 4, 2, 6, 9, 3, 8]
print(list(filter(lambda x: x%2==0, l4)))
print('*'*80)

# zip: 压缩
print(list(zip('abcdef', [1, 2, 3, 4, 5, 6])))