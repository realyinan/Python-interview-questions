# Python中classmethod与staticmethod的区别

class Person():
    # 魔法方法
    # 构造函数: 初始化方法
    def __init__(self, name):
        self.name = name

    # 对象方法: 成员方法
    def run(self):
        pass
    
    # 私有方法
    def __eat(self):
        pass

    # 类方法
    # 1. 类方法中有cls, 就是Person类, 可以调用类中的类属性, 类方法, 静态方法
    # 2. 可以使用对象和类来调用类方法, 建议使用类来调用
    # 3. 类方法中没有self, 不能调用对象属性, 对象方法, 私有方法
    @classmethod
    def sing(cls):
        print(cls==Person)
        print('classmethod')

    # 静态方法
    # 1. 静态方法中没有cls, 不可以调用类属性, 类方法, 静态方法
    # 2. 可以使用对象和类来调用静态方法, 建议使用类来调用
    # 3. 静态方法中没有self, 不能调用对象属性, 对象方法, 私有方法
    @staticmethod
    def dance():
        print('staticmethod')

# 类调用
Person.sing()
Person.dance()
print('*'*100)

# 对象调用
p = Person('zhangsan')
p.sing()
p.dance()