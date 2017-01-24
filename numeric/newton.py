def newton(f, dx, x0, n):
    x = x0
    for i in range(0, n):
        x = x - f(x) / dx(x)

    return x
