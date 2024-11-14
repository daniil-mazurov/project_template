"""Список исключений приложения"""


class BaseError(Exception):
    """Базовый класс для ошибок.

    Args:
        text (str): Сообщение об ошибке. Defaults to "Ошибка работы".
    """

    def __init__(self, text="Ошибка работы") -> None:
        super().__init__(text)
