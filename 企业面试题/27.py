# 对下面给出的字典按值从大到小对键进行排序。

my_dict = {
    'APPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

for n in my_dict:
    print(n)

# 第一种方法
# li = list(my_dict.items())
# li.sort(key=lambda x: x[1], reverse=True)
# my_dict = {key: value for key, value in li}
# print(my_dict)

# 第二种方法
# li = list(my_dict.items())
# res = sorted(li, key=lambda x: x[1], reverse=True)
# my_dict = {key: value for key, value in res}
# print(my_dict)

# 第三种方法
res = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)
print(res)
res2 = {key: my_dict[key] for key in res}
print(res2)