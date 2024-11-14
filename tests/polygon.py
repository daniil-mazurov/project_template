import logging
import logging.config
import sys
from pathlib import Path

sys.path.insert(1, str(Path(__file__).parents[1] / "src"))

from core.config import settings

logging.config.fileConfig("log.ini", disable_existing_loggers=False)
logger = logging.getLogger()


logger.info(f"{settings.PARAM=}")
