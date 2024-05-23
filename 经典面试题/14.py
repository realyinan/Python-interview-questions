# Python中变量在内存中的存储方式

# 不可变类型: int float str tuple
# 可变类型: list dict set

# 不可变类型
s = 'hello'
print(id(s))  # 2772222315312
s2 = 'hello'
print(id(s2))  # 2772222315312
s2 = 'hello2'
print(id(s2))  # 2772222315184
print('*'*100)

# 可变类型
list1 = [1, 2, 3]
print(id(list1))  # 2947212348800
list1.append(4)  
print(id(list1))  # # 2947212348800
print('*'*100)

list1 = [1, 2, 3]
print(id(list1))  # 2574260597632
list2 = [1, 2, 3]
print(id(list2))  # 2574259817856

