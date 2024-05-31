# 写一个函数实现字符串反转，尽可能写出你知道的所有方法

def reverse_string(content):

    # 切片
    return content[::-1]

    # 反转拼接
    return ''.join(reversed(content))

    # 递归
    if len(content) <= 1:
        return content
    return reverse_string(content[1:] + content[0])

    # 反转拼接
    return ''.join([content[i] for i in range(len(content)-1, -1. -1)])
