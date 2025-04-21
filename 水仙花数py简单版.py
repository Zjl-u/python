s=input()
n=len(s)
Sum=0
for i in s:
    Sum+=int(i)**n
if Sum==int(s):
    print(f'{s}是水仙花数')