# __init__和__new__方法有什么区别？

# Python中调用构造器创建对象属于两阶段构造过程，首先执行__new__方法获得保存对象所需的内存空间，再通过__init__执行对内存空间数据的填充（对象属性的初始化）。__new__方法的返回值是创建好的Python对象（的引用），而__init__方法的第一个参数就是这个对象（的引用），所以在__init__中可以完成对对象的初始化操作。

class SquareNumber(int):
    def __new__(cls, value: int):
        return super().__new__(cls, value**2)
    
class Student():
    def __new__(cls, first_name, last_name):
        obj = super().__new__(cls)
        obj.first_name = first_name
        obj.last_name = last_name
        return obj
    
num = SquareNumber(2)
print(num)
print(type(num))
print(isinstance(num, int))
print('*'*100)

student = Student('Jack', "Ma")
print(student.first_name)
print(student.last_name)