"""
根据圆的半径计算周长和面积
"""

# 需要用到python的math模块

import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * (radius**2)
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
