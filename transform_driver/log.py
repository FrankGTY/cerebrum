"""logging."""

from loguru import logger
import os
import sys
import time
from typing import Any

current_time = time.strftime("%Y_%m_%d")
log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")


class Loggings:
    """Write log to log file."""

    __instance = None
    logger.remove()
    logger.add(
        sys.stdout,
        colorize=True,
        enqueue=True,
        level="TRACE",
        format="<green>{time:YYYY-MM-DD hh:mm:ss}</green> | "
        "<level>{level}</level> | <level>{message}</level>",
    )
    logger.add(
        f"{log_path}/{current_time}.log",
        level="DEBUG",
        encoding="utf-8",
        enqueue=True,
        diagnose=False,
        rotation="1 day",
        retention="2 weeks",
    )

    def __new__(cls, *args: Any, **kwargs: Any):
        """Write new method."""
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def trace(self, msg: str):
        """Log level is trace."""
        return logger.trace(msg)

    def debug(self, msg: str):
        """Log level is debug."""
        return logger.debug(msg)

    def info(self, msg: str):
        """Log level is info."""
        return logger.info(msg)

    def success(self, msg: str):
        """Log level is success."""
        return logger.success(msg)

    def warning(self, msg: str):
        """Log level is warning."""
        return logger.warning(msg)

    def error(self, msg: str):
        """Log level is error."""
        return logger.error(msg)

    def critical(self, msg: str):
        """Log level is critical."""
        return logger.critical(msg)
