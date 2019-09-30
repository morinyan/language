"""
判断年份是否为闰年
"""

year = int(input('请输入年份: '))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print('是否为闰年: %s' % is_leap)
