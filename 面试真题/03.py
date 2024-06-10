# 请用Python语言实现功能：输入年月日，判断这一天是这一年的第几天?

import datetime
import time

def dayodyear():
    year = int(input('请输入年份: '))
    month = int(input('请输入月份: '))
    day = int(input('请输入年份: '))

    date1 = datetime.date(
        year=year,
        month=month,
        day=day
    )

    date2 = datetime.date(year=year, month=1, day=1)

    return (date1 - date2).days + 1


time1 = datetime.datetime.now()
print(time1)
print(time1.strftime('%Y-%m-%d'))
print('*'*100)
time2 = time.time()
print(time2)
time3 = time.ctime(time2)
print(time3)
