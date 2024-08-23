def validate(user_name: str) -> bool:
    if len(user_name) < 5:
        return False

    if len(user_name) > 10:
        return False

    if '@' in user_name:
        return False

    return True

