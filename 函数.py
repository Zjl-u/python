# Python 3.4 兼容版本 - 正立等腰三角形
n = int(input())

for i in range(1, n + 1):
    # 计算左侧空格数
    spaces = ' ' * (i-1)
    # 计算星号数
    stars = '*' * (n-i+1)
    # 拼接并打印
    print(spaces + stars)