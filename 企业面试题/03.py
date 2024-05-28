# 写一个删除列表中重复元素的函数，要求去重后元素相对位置保持不变
alist = [2, 3, 2, 1, 1, 5, 6, 7, 3]

alist2 = list(set(alist))
alist2.sort(key=alist.index)
print(alist2)

print(sorted(set(alist), key=alist.index))

alist3 = []

for i in alist:
    if i not in alist3:
        alist3.append(i)
print(alist3)

