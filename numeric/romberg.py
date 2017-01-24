import numpy
from math import cos
from math import pi


def t_0_k(a, b, f, k):
    p = 2 ** k
    res = f(a) + f(b)
    h_k = (b - a) / p
    for i in range(1, p - 1):
        res += 2 * f(a + i * h_k)
    res *= h_k / 2
    return res


def t_m_k(m, k, R):
    p = 4 ** m
    return (p * R[m][k - 1] - R[m - 1][k - 1]) / (p - 1)


def romberg(a, b, f, N):
    R = numpy.zeros((15, 15))
    for i in range(0, N):
        R[i][0] = t_0_k(a, b, f, i)

    for x in range(1, N):
        for y in range(1, x + 1):
            R[x][y] = t_m_k(x, y, R)

    return R[N - 1][N - 1]


def f(x):
    return 2017 * x ** 6 - 2016 * x ** 5 + 2015 * x ** 2 - 2014


def g(x):
    return 1 / (1 + x ** 2)


def h(x):
    return cos(x) / x


print(romberg(-2, 3, f, 15))
print(romberg(-5, 5, g, 15))
print(romberg(pi, 30, h, 15))
