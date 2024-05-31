# 如何读取大文件，例如内存只有4G，如何读取一个大小为8G的文件
def get_lines():
    with open(r'企业面试题\file.txt', 'r') as f:
        while True:
            part = f.read(10)
            if part:
                yield part
            else:
                return None

for e in get_lines():
    print(e)
    print('---')
