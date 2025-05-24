def f2(n, result):
    if n == 0:
        return 0
    else:
        return f2(n - 1, n + result)

print(f2(2, 0))