# 有一个通过网络获取数据的函数（可能会因为网络原因出现异常），
# 写一个装饰器让这个函数在出现指定异常时可以重试指定的次数，并在每次重试之前随机延迟一段时间，
# 最长延迟时间可以通过参数进行控制。

from functools import wraps
import random
import time

def retry(*args, retry_time=3, max_wait_sec=5, errors=(Exception,)):
    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(retry_time):
                try:
                    return fn(*args, **kwargs)
                except errors:
                    time.sleep(random.random() * max_wait_sec)
            return None
        return wrapper
    return retry


@retry(retry_time=4, max_wait_sec=4)
def request_():
    pass


