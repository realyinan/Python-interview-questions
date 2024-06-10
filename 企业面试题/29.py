# 写一个函数，传入的参数是一个列表（列表中的元素可能也是一个列表），返回该列表最大的嵌套深度。例如：列表[1, 2, 3]的嵌套深度为1，列表[[1], [2, [3]]]的嵌套深度为3。

def list_depth(lst):
    if not isinstance(lst, list):
        return 0
    elif not lst:
        return 1
    else:
        return 1 + max(list_depth(i) for i in lst)

print(list_depth([[1], [2, [3]]]))


