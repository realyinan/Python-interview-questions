# 阅读下面的代码，写出程序的运行结果。
class Person():
    x = 1

class Child1(Person):
    pass

class Child2(Person):
    pass

print(Person.x, Child1.x, Child2.x)
Child1.x = 2
print(Person.x, Child1.x, Child2.x)
Person.x = 3
print(Person.x, Child1.x, Child2.x)
