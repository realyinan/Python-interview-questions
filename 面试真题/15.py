# Python中如何交换两个变量的值?

a = 100
b = 200

# 方法一
# a, b = b, a
# print(a, b)

# 方法二
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a, b)

# 方法三
# c = a
# a = b
# b = c
# print(a, b)

# 方法四
a = a + b
b = a - b
a = a - b
print(a, b)