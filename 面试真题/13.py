# 函数调用参数的传递方式是值传递还是引用传递?

# 不可表类型是值传递
def fn(n):
    n += 1
    print(n)

n = 100
fn(n)
print('n:', n)

# 可变类型是引用传递
def fn2(alist):
    alist.append(4)
    print(alist)

alist = [1, 2, 3]
fn2(alist)
print('alist:', alist)