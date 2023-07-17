TOKEN = "Some_secret_key"


class InvalidTokenException(Exception):
    """
        Your passed invalid token, system cant be used
    """


def check_token(token: str) -> bool:
    if token == TOKEN:
        return True
    raise InvalidTokenException("Your token is wrong")
