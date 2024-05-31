# 说出下列代码的运行结果
class A:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value
    
obj = A(1)
print(obj.value)
print(obj.__value)