"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

import random
ans = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = int(input('请输入: '))
    if num < ans:
        print('大一点')
    elif num > ans:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % count)
if count > 7:
    print('你的智商余额明显不足!')
    
