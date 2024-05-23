# Python中while-else,for-else语法的用法并举例
# Python中的for、while循环都有一个可选的else分支，在循环迭代正常完成之后执行
# 这里的“正常结束”指的是循环遍历了所有的项而没有被 break 语句中断。如果循环因为 break 语句提前退出，那么 else 块不会被执行。

# 经典算法-判断一个数是否是素数
# 素数: 1和本身整除

n = int(input('请输入一个正整数'))

for i in range(2, n):
    if n % i == 0:
        print(f"不是素数")
        break
else:
    print('是素数')
