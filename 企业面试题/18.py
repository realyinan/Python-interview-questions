# 阅读右侧的代码说出运行结果
class A():
    def who(self):
        print('A', end=' ')

class B(A):
    def who(self):
        super().who()
        print('B', end=' ')

class C(A):
    def who(self):
        super().who()
        print('C', end=' ')

class D(B, C):
    def who(self):
        super().who()
        print('D', end=' ')

# MRO 方法解析顺序
print(D.__mro__)
d = D()
d.who()