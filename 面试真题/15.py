# Python中如何交换两个变量的值?

a = 100
b = 200

# 方法一
# a, b = b, a
# print(a, b)

# 方法二
a = a ^ b  
b = a ^ b  # a0 ^ b0 ^ b0 = a0 ^ 0 = a0
a = a ^ b  # a0 ^ b0 ^ a0 = b0
print(a, b)

# 方法三
# c = a
# a = b
# b = c
# print(a, b)

# 方法四
a = a + b  # a0 + b0
b = a - b  # a0 + b0 - b0 = a0
a = a - b  # a0 + b0 - a0 = b0
print(a, b)