names = ["Andrea", "Aaslay", "Steven", "Joa"]
lists = []
for name in names:
    if name.count('a') >= 2:  # 字符串方法count用于计算子字符串在字符串中出现的次数
        lists.append(name)

print(lists)