# 要求：设计一个装饰器函数，如果被装饰的函数返回字符串则将字符串每个单词首字母大写


def Decorator(fun):
    def inner(*args, **kwargs):
        res = fun(*args, **kwargs)
        if isinstance(res, str):
            return res.title()
    return inner

@Decorator
def fun():
    return 'hello world'

print(fun())