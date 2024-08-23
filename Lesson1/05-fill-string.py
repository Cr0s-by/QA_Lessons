# добавить между символами  строк подстроку
from asserts import assert_true


# Вариант 1
def fill_string(source_str: str, add_str: str) -> str:
    res = add_str.join(source_str)
    return res


# Вариант 2
def fill_string(source_str: str, add_str: str) -> str:
    res = ""
    for i in range(len(source_str)):
        res += source_str[i] + add_str
    return res[: -len(add_str)]


# =============================================
# блок проверки

assert_true(fill_string("abc", "1") == "a1b1c")
assert_true(fill_string("abcd", "12") == "a12b12c12d")
assert_true(fill_string("a", "1") == "a")
