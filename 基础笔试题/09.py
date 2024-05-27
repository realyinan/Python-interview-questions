import re
str1 = "Python's features"
str2 = re.match(r'(.*)on(.*) .*', str1, flags=re.M|re.I)  
print(str2)
print(str2.group(2))
print('*'*100)


# 贪婪模式：尽可能多地匹配字符。量词不带 ? 的情况。
# 示例：.*, .+, .{m,n}
# 非贪婪模式：尽可能少地匹配字符。量词带 ? 的情况。
# 示例：.*?, .+?, .{m,n}?


pattern_greedy = r'\[.*\]'
text = '[first] and [second]'

match_greedy = re.search(pattern_greedy, text)
if match_greedy:
    print(match_greedy.group())  # 输出: [first] and [second]


pattern_non_greedy = r'\[.*?\]'
text = '[first] and [second]'

match_non_greedy = re.search(pattern_non_greedy, text)
if match_non_greedy:
    print(match_non_greedy.group())  # 输出: [first]

print('*'*100)

# re.I 忽略大小写 re.M换行匹配

# 匹配每行的开头
pattern = r'^\w+'  # 匹配每行的第一个单词
text = """Line 1: Hello
Line 2: World
Line 3: Python"""
print(re.findall(pattern, text, re.M))

# 忽略大小写匹配
pattern = r'apple'
text = "I have an Apple."
print(re.search(pattern, text, re.I))

