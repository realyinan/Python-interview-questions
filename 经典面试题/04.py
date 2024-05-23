# Python中正则表达式如何提取数据
import re

# 分组()
# 捕获: group, groups, findall()
s = '0755-56789999'
pattern = r'(\d{4})-(\d{8})'
res = re.search(pattern=pattern, string=s)

# 提取数据的第一种方式
print(res)
print(res.group())  # 0755-56789999
print(res.group(1))  # 0755
print(res.group(2))  # 56789999
print(res.groups())  # ('0755', '56789999')
print('*'*100)


# 第二种方式
print(re.findall(pattern=pattern, string=s))  # 返回一个列表