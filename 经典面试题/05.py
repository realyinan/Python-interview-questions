# Python中args与kwargs的用法与区别
# 1. *args中args是元组，可以通过args元组获取所有位置参数
# 2. **kwargs中的kwargs是字典，可以通过kwargs获取所有关键字参数
# 3. 在函数的形参中，如果同时有*args和**kwargs，*args必须在**kwargs前面

def demo(*args):
    print(args)
    print(type(args))

demo(1, 2, 3)
print('*'*100)

def demo2(**kwargs):
    print(kwargs)
    print(type(kwargs))

demo2(a=1, b=2, c=3)
print('*'*100)

def demo3(a, b, *args, c=5,  d=6, **kwargs):
    print(args)
    print(kwargs)

demo3(1, 2)
demo3(1, 2, 3, 4)
demo3(1, 2, 3, 4, 5, c=6, d=7)
demo3(1, 2, 3, 4, 5, c=6, d=7, e=8, f=9)
print('*'*100)


# 通用装饰器
def outer(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
    return inner

# 实参中的*args, **kwargs
a = [1, 2, 3, 4]

def demo4(*args):
    print(args)

demo4(a)  # ([1, 2, 3, 4], )
demo(*a)  # (1, 2, 3, 4)
print('*'*100)


def demo5(**kwargs):
    print(kwargs)

b = {'name': 'kunkun', 'age': 22}
demo5(b=b)  # {'b': {'name': 'kunkun', 'age': 22}}
demo5(**b)
demo5(name='kunkun', age=20)



















