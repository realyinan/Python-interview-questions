# 请写出一段python代码实现删除list里面的重复元素?

# list.sort() 是 Python 中的一个方法，用于对列表进行就地排序（即直接修改原列表）。这个方法有几个可选参数，可以控制排序的行为。
# list.sort() 方法会直接修改原列表，如果你不想修改原列表，可以使用内置函数 sorted()，它会返回一个新的已排序列表。

# 不保证顺序
alist = [2, 4, 1, 2, 1, 5, 7, 4]
print(list(set(alist)))
print('*'*100)

# 保证顺序
alist2 = []
for i in alist:
    if i not in alist2:
        alist2.append(i)
print(alist2)
print('*'*100)

l1 = list(set(alist))
l1.sort(key=alist.index)
print(l1)
print(sorted(l1, key=alist.index))


