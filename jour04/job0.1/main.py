def exposant(x, n):
    if n == 0:
        return 1
    else:
        return x * exposant(x, n - 1)
    
print(exposant(5, 2))