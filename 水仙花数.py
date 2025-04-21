x=int(input('请输入数字'))
i=j=x
n=Sum=0.0
while i>0:
    middle=i%10
    i=i//10
    n+=1
while j>0:
    wei=j%10
    j=j//10
    Sum+=wei**n
if Sum==x:
    print(f'{x}是水仙花数')
else:
    print(f'{x}不是水仙花数')