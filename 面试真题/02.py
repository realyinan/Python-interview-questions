# 类中@property装饰器有什么用 

# @property 装饰器在Python中用于将类的方法转换为只读属性。它使得可以像访问属性一样调用方法，从而提高代码的可读性和封装性。通过使用 @property，我们可以定义一个方法，但通过点符号访问它时，看起来像是直接访问一个属性。
 
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property  # 使用@property将方法变为属性
    def radius(self):
        return self._radius

    @property  # 将方法变为只读属性
    def area(self):
        return 3.14159 * (self._radius ** 2)

    @radius.setter  # 可选，如果需要可写属性，可以使用@<property_name>.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = value


c = Circle(5)
print(c.radius)  # 输出: 5
print(c.area)    # 输出: 78.53975
print('*'*100)

c.radius = 10
print(c.radius)  # 输出: 10
print(c.area)    # 输出: 314.159
