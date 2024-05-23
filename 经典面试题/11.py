# 如何在不改变原有list顺序的前提下,去除该list中的重复数据

list1 = [1, 2, 2, 6, 3, 4, 2, 2, 2, 2, 1, 1, 1, 1, 2]

# 去重 set 无序
print(list(set(list1)))
print('*'*100)

# 有序
i = 0
while i < len(list1):

    j = i + 1
    while j < len(list1):
        if list1[j] == list1[i]:
            list1.pop(j)
            j -= 1
        j += 1

    i += 1

print(list1)
print('*'*100)


# 有序 方法二
list2 = [1, 2, 2, 6, 3, 4, 2, 2, 2, 2, 1, 1, 1, 1, 2]
list3 = []

for i in list2:
    if i not in list3:
        list3.append(i)
print(list3)
print('*'*100)

