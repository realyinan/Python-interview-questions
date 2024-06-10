lists = [1, 2, 3, 4]
tmp = 0
for i, j in enumerate(lists, start=2):
    tmp += i*j

print(tmp)