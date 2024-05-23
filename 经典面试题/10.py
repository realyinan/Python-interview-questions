# 在编程中，深拷贝和浅拷贝是两种复制对象的方式，它们在处理复杂对象时有很大的不同。

# 1. **浅拷贝**（Shallow Copy）：
#    - 浅拷贝只复制对象的顶层，如果对象中还包含了对其他对象的引用，浅拷贝不会复制被引用的对象，而是仅仅复制引用。
#    - 这意味着，如果原始对象中的一个可变项被改变，这个改变也会反映到浅拷贝的对象上。
#    - 在Python中，你可以使用`copy()`方法或`copy.copy()`函数来进行浅拷贝。

# 2. **深拷贝**（Deep Copy）：
#    - 深拷贝会复制对象内部的所有层次，不仅复制对象本身，还包括对象中引用的所有对象。
#    - 这样，深拷贝生成的新对象和原始对象完全独立，对新对象的修改不会影响到原始对象。
#    - 在Python中，可以使用`copy.deepcopy()`函数来进行深拷贝。

# 在使用这些拷贝方法时，要考虑到你的具体需求，因为深拷贝可能会涉及更多的内存使用和计算成本。
import copy

# 赋值
list1 = [1, 2, 3]
list2 = list1
list2[0] = 99
print(list1, list2)  # [99, 2, 3] [99, 2, 3]
print('-'*100)

# 浅拷贝
list1 = [1, 2, 3]
list2 = list1.copy()
list2[0] = 99
print(list1, list2)
print('-'*100)

# 浅拷贝列表嵌套
list1 = [1, 2, [3, 4]]
list2 = list1.copy()
list2[0] = 99
print(list1, list2)
print('-'*100)

list1 = [1, 2, [3, 4]]
list2 = list1.copy()  # 浅拷贝
list2[-1][-1] = 99
print(list1, list2)
print('-'*100)


# 深拷贝
list1 = [1, 2, [3, 4]]
list2 = copy.deepcopy(list1)  # 浅拷贝
list2[-1][-1] = 99
print(list1, list2)
print('-'*100)
