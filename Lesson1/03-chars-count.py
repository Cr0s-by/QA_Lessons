# Функция подсчета символа в строке без учета регистра
# Подсказка: используйте функцию lower

from asserts import assert_true


def chars_count(str_value: str, char: str, case_sensitive: bool) -> int:
    cnt = 0
    if case_sensitive == False:
        for c in str_value.lower():
            if c == char.lower():
                cnt += 1
    else:
        for c in str_value:
            if c == char:
                cnt += 1
    return cnt


# =============================================
# блок проверки


assert_true(chars_count("12345qQ", "q", False) == 2)
assert_true(chars_count("12345qQ", "Q", False) == 2)
assert_true(chars_count("12345qQ", "q", True) == 1)
