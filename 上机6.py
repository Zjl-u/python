def xfunction(n):
    if n == 1:
        return 1;
    else:
        return n + xfunction(n - 1)

print(xfunction(4))