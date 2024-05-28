# 不使用中间变量，交换两个变量a和b的值
a = 100
b = 200

a, b = b, a

# a = a ^ b  
# b = a ^ b  # a0 ^ b0 ^ b0 = a0
# a = a ^ b  # a0 ^ b0 ^ a0 = b0

# a = a + b
# b = a - b  # a0+b0-b0=a0
# a = a - b  # a0+b0-a0=b0

print(a, b)