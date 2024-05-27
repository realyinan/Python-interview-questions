# 手写一个判断函数时间的装饰器
import time

def outer(fn):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        end_time = time.time()
        print(end_time-start_time)
        return res
    return inner

@outer
def fn():
    time.sleep(3)

fn()