from math import floor


def euklides(a, b):
    a0 = a
    b0 = b

    # init
    p = 1
    q = 0
    r = 0
    s = 1

    while b != 0:
        x = a % b
        y = floor(a / b)

        a = b
        b = x

        r_t = r
        s_t = s
        r = p - y * r
        s = q - y * s
        p = r_t
        q = s_t

    return p * a0 + q * b0


print(euklides(13, 17))
