# 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序

d= {'a':24,'g':52,'i':12,'k':33}
print(d.items())
print(list(d.items()))
res = sorted(list(d.items()), key=lambda x: x[1])
print(res)

d2 = {key: value for key, value in res}
print(d2)