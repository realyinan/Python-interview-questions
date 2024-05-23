import re
str1 = "Python's features"
str2 = re.match(r'(.*)on(.*?) .*', str1, flags=re.M|re.I)
# print(str2)
print(str2.group(2))

# 贪婪模式：尽可能多地匹配字符。量词不带 ? 的情况。
# 示例：.*, .+, .{m,n}
# 非贪婪模式：尽可能少地匹配字符。量词带 ? 的情况。
# 示例：.*?, .+?, .{m,n}?


# 在Python的正则表达式模块 re 中，group() 方法用于提取匹配对象中的特定部分。group() 方法是 re.Match 对象的一部分，该对象是通过使用 re 模块中的匹配函数（如 search、match 或 findall）获得的。

import re

pattern_greedy = r'\[.*\]'
text = '[first] and [second]'

match_greedy = re.search(pattern_greedy, text)
if match_greedy:
    print(match_greedy.group())  # 输出: [first] and [second]


import re

pattern_non_greedy = r'\[.*?\]'
text = '[first] and [second]'

match_non_greedy = re.search(pattern_non_greedy, text)
if match_non_greedy:
    print(match_non_greedy.group())  # 输出: [first]
