import logging
import logging.config
import os
import sys

sys.path.insert(1, os.path.join(os.path.dirname(sys.path[0]), "src"))


from core.config import settings

logging.config.fileConfig("log.ini", disable_existing_loggers=False)
logger = logging.getLogger()


logger.info(f"{settings.param_name=}")
