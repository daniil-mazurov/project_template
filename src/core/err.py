"""Функционал обработки ошибок"""

import logging
import os
from functools import wraps

from core.exceptions import BaseError

logger = logging.getLogger()


def get_args_dict(fn, args, kwargs):
    """Создает словарь аргументов для функции.

    Args:
        fn (function): Функция, для которой необходимо получить аргументы.
        args (tuple): Позиционные аргументы функции.
        kwargs (dict): Именованные аргументы функции.

    Returns:
        dict: Словарь аргументов, где ключи - имена параметров, а значения - переданные значения.
    """
    args_names = fn.__code__.co_varnames[: fn.__code__.co_argcount]
    return {**dict(zip(args_names, args)), **kwargs}


def exception_logging(
    ignore_raise=False,
    custom_exception=Exception,
    message="Something went wrong",
):
    """Декоратор для логирования исключений, возникающих в синхранных функциях.

    Args:
        ignore_raise (bool, optional): Прерывать ли выполнение программы при возникновении исключения. Defaults to False.
        custom_exception (Exception, optional): Тип исключения, который нужно обрабатывать. Defaults to Exception.
        message (str, optional): Сообщение для логирования при возникновении исключения. Defaults to "Something went wrong".

    Returns:
        function: Обернутая функция с логированием исключений.
    """

    def __exception_logging(func):
        old_factory = logging.getLogRecordFactory()

        def record_factory(*args, **kwargs):
            """Создает запись лога с информацией о функции."""
            record = old_factory(*args, **kwargs)
            if hasattr(func, "__wrapped__"):
                record.funcName = func.__wrapped__.__name__
                record.filename = os.path.basename(
                    func.__wrapped__.__code__.co_filename
                )
                record.lineno = func.__wrapped__.__code__.co_firstlineno
            else:
                record.funcName = func.__name__
                record.filename = os.path.basename(func.__code__.co_filename)
                record.lineno = func.__code__.co_firstlineno
            return record

        @wraps(func)
        def wrapper(*args, **kwargs):
            """Обертка для функции с обработкой исключений."""
            try:
                result = func(*args, **kwargs)
            except custom_exception as e:
                logging.setLogRecordFactory(record_factory)

                signature = get_args_dict(func, args, kwargs)
                logger.debug(f"function {func.__name__} called with args {signature}")
                logger.exception(f"{message}\nError:\n")

                logging.setLogRecordFactory(old_factory)

                if not ignore_raise:
                    raise BaseError from e
            else:
                return result

        return wrapper

    return __exception_logging
