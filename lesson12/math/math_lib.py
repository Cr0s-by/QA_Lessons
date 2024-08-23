def add(x1, x2):
    return x1 + x2


def sub(x1, x2):
    return x1 - x2


def mul(x1, x2):
    return x1 * x2


def div(x1, x2):
    if x2 == 0:
        raise ZeroDivisionError()

    return x1 / x2
