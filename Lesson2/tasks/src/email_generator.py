import re


def generate_email(user_name: str, domain: str) -> str:
    fixed_user_name = re.sub(r'[\@\#\$\%\^\&\*\(\)]', '_', user_name)
    return fixed_user_name + '@' + domain
