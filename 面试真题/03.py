# 请用Python语言实现功能：输入年月日，判断这一天是这一年的第几天?

import datetime

def dayodyear():
    year = int(input('请输入年份: '))
    month = int(input('请输入月份: '))
    day = int(input('请输入年份: '))

    date1 = datetime.date(
        year=year,
        month=month,
        day=day
    )
    print(date1)
    print(date1)

    date2 = datetime.date(year=year, month=1, day=1)

    print(date2)

    return (date1 - date2).days + 1

print(dayodyear())