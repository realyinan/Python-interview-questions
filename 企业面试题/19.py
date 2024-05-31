# Python中如何实现字符串替换操作？
import re

str1 = "Hello World"
str2 = str1.replace("World", "Python")
print(str2)

pattern = r'\d{2}'
source = "I'm 80 years old"
str3 = re.sub(pattern, "20", source)
print(str3)
