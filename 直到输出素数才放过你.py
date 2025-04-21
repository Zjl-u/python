m = int(input())
while m>0:
    flag = 1
    for i in range(2,m):
        if(m%i==0):
            flag=0
            break
    if(flag==1):
        print(f'{m}是素数')
        break
    m = int(input())

