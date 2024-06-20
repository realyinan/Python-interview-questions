import datetime

# 获取当前日期和时间
now = datetime.datetime.now()
print(now)
print('*'*100)

# 创建日期和时间对象
dt = datetime.datetime(2024, 6, 11, 15, 24, 36)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print('*'*100)

# 格式化日期和时间
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
print('*'*100)

# 日期之间的计算
print(dt + datetime.timedelta(days=10))
print('*'*100)

# 创建日期对象
dt = datetime.date(2024, 6, 4)
print(dt)
print('*'*100)

# 创建时间对象
dt = datetime.time(15, 30, 23)
print(dt)
print('*'*100)

# 获取当前日期
dt = datetime.date.today()
print(dt)
print('*'*100)

# 获取当前时间
dt = datetime.datetime.now().time()
print(dt)