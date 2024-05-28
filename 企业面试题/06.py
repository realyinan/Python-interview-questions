# 说一下你对Python中迭代器和生成器的理解

def geneator(n):
    for i in range(n):
        yield i**2

j = geneator(10)
# for i in j:
#     print(i)
print(next(j))
print(next(j))
print(next(j))

