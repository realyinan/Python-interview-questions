# 使用Python代码实现遍历一个文件夹的操作

import os
def print_dir_content(spath):
    s_child_list = os.listdir(spath)
    for s_child in s_child_list:
        s_child_path = os.path.join(spath, s_child)
        if os.path.isdir(s_child_path):
            print_dir_content(s_child_path)
        else:
            print(s_child_path)

 

print_dir_content(r"C:\Users\19981\Desktop\复习")
        

