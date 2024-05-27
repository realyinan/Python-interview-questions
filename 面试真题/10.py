# 写一个函数找出一个整数数组中，第二大的数

alist = [1, 2, 3, 4, 9, 9, 8, 8]

list2 = sorted(set(alist))
print(list2[-2])
