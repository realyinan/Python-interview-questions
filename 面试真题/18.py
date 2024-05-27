# 简述可迭代对象和迭代器之间的区别和联系

# 可迭代对象是可以被迭代的对象(如列表、元组等)，它们实现了 __iter__() 方法。
# 可以通过 iter() 函数将其转换为迭代器。

# 迭代器是可以记住遍历位置的对象，实现了 __iter__() 和 __next__() 方法，且可以通过 next() 函数获取下一个元素
# 迭代器是一个可迭代对象, 可迭代对象不一定是一个迭代器 
# 生成器即使可迭代对象, 还是一个迭代器

# 可迭代对象
my_list = [1, 2, 3]
for i in my_list:
    print(i)

# 迭代器
my_iter = iter(my_list)
for j in my_iter:
    print(j)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

