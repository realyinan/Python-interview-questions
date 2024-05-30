# 写一个函数统计传入的列表中每个数字出现的次数并返回对应的字典
# 字典的 get 函数是 Python 字典对象的一个方法，用于安全地获取字典中的值。如果指定的键不存在于字典中，get 方法会返回一个默认值（默认情况下为 None），而不会引发 KeyError 异常。

li = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 'A', 'b']

def count_items(items):
    d = {}
    for item in items:
        if isinstance(item, (int, float)):
            d[str(item)] = d.get(item, 0) + 1
    return d

res = count_items(li)
print(res)

