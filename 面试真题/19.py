# 有一个文件file.txt大小约为10G，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不变的情况下，应该如何实现? 需要考虑的问题都有那些?

# 生成器在需要的时候才生成数据，而不是一次性把所有数据都生成并存储在内存中。这样可以大大减少内存的使用，特别是当处理大数据集时。由于生成器一次只在内存中保留一个数据项，而不是将所有数据都存储在内存中，因此它们非常适合处理大文件或大数据集。

def get_lines():
    with open(r'面试真题\file.txt', 'rb') as f:
        # return f.readlines()

        # 分段读取
        while True:
            part = f.read(10)
            if part:
                yield part
            else:
                break
    
def process(e):
    print('e:', e)

if __name__ == '__main__':
    for e in get_lines():
        process(e)
