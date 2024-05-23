# Python中list,set,dict,tuple的区别

# list和tuple属于序列，可以使用下标访问，可以进行切片操作，可以排序
# list用[]定义，tuple用（）定义
# list是可变容器，可以修改其中的元素，tuple属于不可变容器，不能修改元素
# tuple属于不可变容器，没有深拷贝和浅拷贝，list有深拷贝和浅拷贝
# list一般不做函数参数的默认值，tuple可以做函数参数的默认值


# set和dict不属于序列，无序，不能通过下标访问，但set和dict也有区别
# dict可以通过key访问，set不行
# dict键不可以重复，值可以重复，set不允许有重复元素
# dict可以根据键修改值，set不能修改元素