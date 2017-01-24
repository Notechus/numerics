from math import pow


def bernstein(n, i, x):
    return bc(n, i) * pow(x, i) * pow(1 - x, n - i)


def bc(n, k):
    res = 1
    for i in range(1, k):
        res *= (n - i + 1) / i
    return res


x = [0.0, 3.5, 25.0, 25.0, -5.0, -5.0, 15.0, -0.5, 19.5, 7.0, 1.5]
y = [0.0, 36.0, 25.0, 1.5, 3.0, 33.0, 11.0, 35.0, 15.5, 0.0, 10.5]

waga = [1, 2, 4, 2, 3, 4, 2, 1, 5, 4, 1]


def bezier(t, n):
    res_x = 0.0
    res_y = 0.0
    mianownik = 0.0

    for i in range(0, n + 1):
        mianownik += waga[i] * bernstein(n, i, t)

    for i in range(0, n + 1):
        res_x += waga[i] * x[i] * bernstein(n, i, t)

    for i in range(0, n + 1):
        res_y += waga[i] * y[i] * bernstein(n, i, t)

    return (res_x / mianownik, res_y / mianownik)


n = 10
punkty = []
for z in range(0, 101):
    t = z / 100.0
    punkty.append(bezier(t, n))

for i in range(0, 101):
    print(str(punkty[i][0]) + ',' + str(punkty[i][1]) + ';')
