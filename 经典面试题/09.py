# 装饰器
# 对Python装饰器的理解:
    # 1、装饰器的实现是由闭包支撑的
    # 2、装饰器本质上是一个python函数，它可以在让其他函数在不需要做任何代码的变动的前提下增加额外的功能
    # 3、装饰器的返回值也是一个函数的对象，该函数对象就是添加额外功能后的与原函数同名的函数

# 装饰器
def outer(fn):
    def inner():
        print("before")
        fn()
        print("after")
    return inner

# 被装饰的函数
@outer
def sing():
    print('唱歌')

sing()

# 装饰器的原理
# sing = outer(sing)
# sing()
print('*'*100)

# 通用装饰器
def outer1(fn):
    def inner(*args, **kwargs):
        print('before')
        res = fn(*args, **kwargs)
        print('after')
        return res
    return inner

@outer1
def dance(name):
    print(f'跳{name}舞')
    return 100

res = dance('芭蕾')
print(res)
