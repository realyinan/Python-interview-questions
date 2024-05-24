# Python中的内存管理机制是怎样的

# 垃圾回收: GC
#    引用计数
# 垃圾: 占用了但是不会再使用的内存


import sys

list1 = [1, 2]
print(sys.getrefcount(list1))  # 2

list2 = list1
print(sys.getrefcount(list1))  # 3

list3 = list1
print(sys.getrefcount(list1))  # 4

list3 = 10
print(sys.getrefcount(list1))  # 3

list2 = 5
print(sys.getrefcount(list1))  # 2

list1 = 3  # 此时已经没有任何变量指向[1, 2], 引用计数为0

# 引用计数为0, 垃圾回收机制则会在某个时刻把内存快速释放


# 内存池
# Level+3层：Python内置对象（如：int,dict）都有独立的私有内存池
# Level+2层：当申请的内存 < 256KB时（小内存），内存分配主要由Python对象
# Level+1层：当申请的内存 > 256KB时（大内存），会由内部的C标准库的malloc创建对象

# 内存池解决了： 如果对象（尤其是对小整数的使用）频繁的创建和销毁， 就会产生很多内存碎片，最终会影响系统的性能
