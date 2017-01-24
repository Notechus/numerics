def bisect(f, a, b, n):
    if f(a) == 0.0:
        return a
    if f(b) == 0.0:
        return b

    m = 0.0
    for i in range(0, n):
        m = (a + b) / 2

        if f(m) == 0.0:
            return m

        if f(a) * f(m) < 0.0:
            b = m
        else:
            a = m
    return m
