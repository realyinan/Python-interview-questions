# 举例说明什么情况下会出现KeyError、TypeError、ValueError

my_dict = {'a': 1, 'b': 2}

# 尝试访问字典中不存在的键
try:
    value = my_dict['c']
except KeyError as e:
    print(f'Keyerror: {e}')

# TypeError 在操作或函数应用于不支持的类型时会抛出。
try:
    res = 'hello' + 5
except TypeError as e:
    print(f"TypeError: {e}")

# ValueError 在操作或函数接收到的参数类型正确但值不合适时会抛出。
try:
    res = int('hello')
except ValueError as e:
    print(f'ValueError: {e}')