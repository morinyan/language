"""
用for循环实现1~100求和
"""

sum = 0
for x in range(100):
    sum += x
print(sum)


"""
用for循环实现1~100之间的偶数求和
"""
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)


