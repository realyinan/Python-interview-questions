# 阅读下面的代码，写出程序的运行结果.

items = [1, 2, 3, 4]
print([item for item in items if item % 2])

print([(x, y) for x, y in zip('abcd', (1, 2, 3, 4, 5))])

# h l l o '' world
# h l o w r d

print(zip([1, 2, 3], ['a', 'b', 'c']))