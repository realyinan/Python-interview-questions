# 简述Python正则表达式中search和match的区别

import re

def test_search():
    pattern = r'\d{2}'
    source = "I'm 80 years old"
    res = re.search(pattern, source)  # 返回第一个
    print(res)  # <re.Match object; span=(4, 6), match='80'>
    print(res.group()) 

def test_match():
    pattern = r'\d{2}'
    source = "I'm 80 years old"
    source = "80 years old"
    res = re.match(pattern, source)  # 从字符串开头开始匹配
    print(res) 
    print(res.group())

def test_fullmatch():
    pattern = r'\d{2}'
    source = '80'
    res = re.fullmatch(pattern, source)
    print(res)
    print(res.group())

# test_search()
# test_match()
test_fullmatch()