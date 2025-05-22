x,y=2,1
def n(a,b):
    a,b=a*a,b*b
    global x
    x,y=5,3
    return a+b+x+y
print(n(2,1),x,y)