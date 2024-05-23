# Python中type与isinstance方法的区别

# 其中type用于获取对象的类型，其返回值是对象的类型；
# isinstance用于测试对象是否是某种类型，返回True或False。区别：

a = 10
print(type(10))

if type(a) == int:
    print('int')
print('*'*100)

b = 1.1
print(isinstance(a, int))
print(isinstance(b, (int, float)))
print('*'*100)


# 继承
class Father():
    pass

class Son(Father):
    pass

if __name__ == '__main__':
    son = Son()
    print(type(son))  # <class '__main__.Son'>
    print(isinstance(son, Son))  # True
    print(isinstance(son, Father))  # True
    print(isinstance(son, object))  # True

