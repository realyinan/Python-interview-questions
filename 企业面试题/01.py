# 在Python中如何实现单例模
def singleton(cls):
    instaces = {}
    def wrapper(*args, **kwargs):
        if cls not in instaces:
            instaces[cls] = cls(*args, **kwargs)
        return instaces[cls]
    return wrapper

# 装饰类
@singleton
class Person():
    def __init__(self, age):
        self.age = age

person1 = Person(1)
person2 = Person(2)
print(person1.age)
print(person2.age)
print(person1 is person2)
