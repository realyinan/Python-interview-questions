# Python中回调函数是如何通信的?

# 回调函数（Callback Function）是一种编程模式中的概念，指的是一个函数被作为参数传递给另一个函数，并在特定的事件或条件下由后者调用。

callback = lambda x: x*10

def callback2(x):
    return x*10

def func(cb):
    # 回调
    res = cb(8)
    print(res)

func(callback)
func(callback2)

