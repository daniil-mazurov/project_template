#!./.venv/bin/python

import logging
import logging.config

from src.app import func
from src.core.metric import speed_metric
from src.parser import parse_args

logging.config.fileConfig("log.ini", disable_existing_loggers=False)
logger = logging.getLogger()


@speed_metric
def start_log():
    """Стартовое сообщение во все лог файлы"""

    for extra_logger in {logger.split(".")[0] for logger in logger.manager.loggerDict}:
        logging.getLogger(extra_logger).info(
            f"<{'=' * 10} {extra_logger.upper()} START {'='*10}>"
        )


def main(args):
    """Точка входа"""

    logger.info(f"<{'=' * 10} MAIN START {'='*10}>", extra=args.__dict__)
    func()
    logger.info(f"<{'=' * 10} MAIN CLOSE {'='*10}>")


if __name__ == "__main__":
    start_log()

    args = parse_args()

    main(args)
