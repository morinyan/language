"""
分段函数求值
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('x = %.2f 的分段函数计算结果: %.2f' % (x, y))
