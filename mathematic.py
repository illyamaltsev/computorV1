
def fabs(x):
    if x < 0:
        x = -x
    return x


def is_int(x):
    if float(x) % 1 == 0:
        return 1
    else:
        return 0


def sqrt(x, eps):
    s = 0.5 * x
    t = s
    s = (s + x / s) * 0.5
    while fabs((s-t)/s) > eps:
        t = s
        s = (s + x / s) * 0.5
    return s
