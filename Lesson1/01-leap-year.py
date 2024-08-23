from asserts import assert_false, assert_true


# Високосные года делятся нацело на 4.
# Однако из этого правила есть исключение: столетия, которые не делятся нацело на 400, високосными не являются.


# Функция вычисления високосного года
def is_leap(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


# =============================================
# блок проверки


def check(year: int, is_leap_value: bool):
    if is_leap_value:
        return assert_true(is_leap(year), "{} является високосным".format(year))

    return assert_false(is_leap(year), "{} не является високосным".format(year))


check(1900, False)
check(2000, True)
check(2001, False)
check(2020, True)
