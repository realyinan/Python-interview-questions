# 闭包
def outer():
    a = 10
    def inner():
        nonlocal a
        a += 1
        print(a)
    return inner

inner = outer()
inner()
inner()
inner()
