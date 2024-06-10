# 阅读下面的代码，写出程序的运行结果.

items = [1, 2, 3, 4]
print([item for item in items if item % 2])

print([(x, y) for x, y in zip('abcd', (1, 2, 3, 4, 5))])

# h l l o '' world
# h l o w r d

print(zip([1, 2, 3], ['a', 'b', 'c']))

# zip 函数是 Python 中一个非常有用的内置函数，它可以将多个可迭代对象（如列表、元组等）“压缩”成一个迭代器，其中每个元素是一个元组，这些元组包含了来自每个可迭代对象中的对应位置的元素。