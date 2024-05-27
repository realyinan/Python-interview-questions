# 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
# split() 函数在 Python 中常用于将字符串分割成子字符串列表。


str1 = "k:1|k1:2|k2:3|k3:4"

def str_to_dict(str1):
    dict1 = {}
    for items in str1.split('|'):
        key, value = items.split(':')
        dict1[key] = int(value)
    return dict1

res = str_to_dict(str1)
print(res)


# 字典推导式
d = {key: int(value) for items in str1.split('|') for key, value in (items.split(':'), )}
print(d)

 