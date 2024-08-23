import functools


def sum_ex(numbers):
    if len(numbers) < 2:
        raise Exception('Недостаточно слагаемых')

    return functools.reduce(lambda a, b: a + b, numbers)


def sum_unless0(numbers):
    if len(numbers) < 2:
        raise Exception('Недостаточно слагаемых')

    s = 0

    for n in numbers:
        if n == 0:
            break

        s += n

    return s
