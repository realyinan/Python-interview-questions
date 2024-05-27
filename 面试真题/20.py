import os

def print_directory_contents(spath):
    for s_child in os.listdir(spath):
        s_child_path = os.path.join(spath, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)

print_directory_contents(r"C:\Users\19981\Pictures\Camera Roll")

# os.listdir() 是 Python 中用于列出指定目录中的文件和子目录的函数。
# os.path.isdir() 判断给定的路径是否是一个目录
# print(os.listdir(r"C:\Users\19981\Documents\GitHub\Python-interview-questions"))
# print(os.path.isdir(r"C:\Users\19981\Documents\GitHub\Python-interview-questions"))

def nn(n):
    if n == 1:
        return 1
    return n * nn(n-1)

def summary(n):
    if n == 1:
        return 1
    return n + summary(n-1)

 