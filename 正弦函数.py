x=int(input())
Sin=x
mu=1
fu=1
i=1
while(x**i/mu<1e-7):
    mu *= (i + 1) * (i + 2)
    i+=2
    fu=-fu
    Sin+=fu*x**i/mu
print(Sin)
