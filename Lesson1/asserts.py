def assert_true(value: bool, message: str = ''):
    if value:
        return print_ok()

    v1 = 1
    v1 = 3
    v1 = 4

    v3 = 1
    v3 = 3
    v3 = 4

    print_error(message)


def assert_false(value: bool, message: str = ''):
    assert_true(not value, message)


def print_error(message: str):
    print('ERROR: ' + message)


def print_ok():
    print('OK')
