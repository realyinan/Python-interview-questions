# 如何使用random模块生成随机数、实现随机乱序和随机抽样？
import random

res = random.random()  # 生成一个范围在[0.0, 1.0)之间的随机浮点数
res = random.uniform(2, 3)  # 从而生成一个范围在 [a, b] 或 [a, b) 之间的浮点数
res = random.randint(4, 10)  # 从而生成一个范围在 [a, b] 或 [a, b) 之间的随机整数
li = [1, 2, 3, 4]
random.shuffle(li)  # 将序列中的元素打乱
res = random.choice(li)  # 可以从非空序列中取出一个随机元素
res = random.sample(li, 3)  # 从总体中抽取一定数量的样本(没有重复的元素)
res = random.choices(li, weights=[0.2, 0.3, 0.4, 0.1], k=4)  # 从总体中抽取一定数量的样本(有重复的元素)
print(res)
