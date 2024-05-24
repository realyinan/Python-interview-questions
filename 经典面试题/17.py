# 你是如何理解Python中的封装,继承,多态的

# 封装: 将属性和方法封装起来
# 继承: 子类去继承父类的属性和方法
# 多态: Python一般不用多态, 没有正真意义上的多态

# 在Python中，继承和调用父类的方法可以通过super()函数来实现。super()函数返回一个父类对象，这样就可以调用父类的方法。在子类中使用super()来调用父类的方法有助于代码的可维护性和复用性。


# 继承
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()  # 调用父类的greet方法
        print(f"I am {self.age} years old.")

# 创建对象并调用方法
child = Child("Alice", 10)
child.greet()
print('*'*100)


class Ipad(object):
    def __init__(self, color):
        self.color = color

    def play_game(self):
        print('玩游戏')

class Iphone(Ipad):
    def __init__(self, color, price):
        super().__init__(color)
        self.price = price

    def call(self):
        print('打电话')


Iphone15 = Iphone('黑色', 10000)
print(Iphone15.color, Iphone15.price)
Iphone15.play_game()
Iphone15.call()
print('*'*100)




# 多态
# 在继承的基础上, 一般有多个子类同时继承一个父类, 让每一个子类去重写父类的同一个方法
# 子类在这个方法上去实现不同的功能. 那么父类对象指向不同子类的时候, 调用该方法则可以实现不同的功能


class Animal():
    def eat(self):
        print('吃东西')

class Dog(Animal):
    def eat(self):
        print('狗吃屎')

class Wolf(Animal):
    def eat(self):
        print('狼吃肉')

class Pig(Animal):
    def eat(self):
        print('猪吃白菜')


class Person():
    def feed(self, animal):
        animal.eat()

dog = Dog()
wolf = Wolf()
pig = Pig()

Person().feed(dog)
Person().feed(wolf)
Person().feed(pig)
