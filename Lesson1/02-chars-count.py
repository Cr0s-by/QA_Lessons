# Функция подсчета символа в строке
from asserts import assert_true


def chars_count(str_value: str, char: str) -> int:
    cnt = 0
    for i in range(len(str_value)):
        if str_value[i] == char:
            cnt += 1

    return cnt


# =============================================
# блок проверки

assert_true(chars_count("12345", "0") == 0)
assert_true(chars_count("12345", "1") == 1)
assert_true(chars_count("12345qq", "q") == 2)
