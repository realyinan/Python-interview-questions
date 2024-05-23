# 请解释Python中with关键字的用法

# 上下文管理器（Context Manager）是 Python 中的一种协议，用于管理资源的分配和释放。最常见的例子就是 with 语句，它确保在代码块执行完毕后，资源会被正确地释放。

# with: 上下文管理器
# __enter__() 进入with代码块前的准备操作
# __exit__() 退出时的善后操作
# 文件对象

# 文件打开: 自动关闭文件
# with open('a.txt') as fp:
#     n = fp.read()


class A():
    def __enter__(self):
        '''初始化操作'''
        print('__enter__')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''做一些善后操作: 比如关闭文件'''
        print('__exit__')
        print(exc_type)  # <class 'ValueError'>
        print(exc_tb)  # <traceback object at 0x00000261FD6CF9C0>
        print(exc_val)  # hello jack

with A() as a:
    print(a)
    raise ValueError('hello jack')

