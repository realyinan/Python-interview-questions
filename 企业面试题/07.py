# 下面这段代码的执行结果是什么

def multify():
    return [lambda x: i * x for i in range(4)]
# 由于 Python 的闭包特性，所有生成的函数共享相同的闭包环境，并且最终的 i 的值是 3，这是循环结束时 i 的值。因此，所有函数会返回 3 * x。
def multify2():
    return [lambda x, i=i: i * x for i in range(4)]

print([m(100) for m in multify()])

# print([m(100) for m in multify2()])
