m,n=eval(input())
max=0
min=0
if m>n:
    max=m
    min=n
else:
    max=n
    min=m
for i in range(min,1,-1):
    if m%i==0 and n%i==0:
        yue=i
        break
for j in range(max,max*min+1,1):
    if j%m==0 and j%n==0:
        bei=j
        break
print(yue,bei)