# 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序

d= {'a':24,'g':52,'i':12,'k':33}

li = sorted(d, key=lambda x: d[x])
d = {key: d[key] for key in li}
print(d)
