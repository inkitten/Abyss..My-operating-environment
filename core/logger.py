"""
logger.py

Creates and returns a logger for any Abyss module.

Example
-------
from core.logger import get_logger

logger = get_logger(__name__)

logger.info("Program started")
logger.warning("Something looks wrong")
logger.error("Database connection failed")
"""

import logging
from pathlib import Path

# Create the logs directory if it doesn't exist.
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


def get_logger(module_name: str):
    """
    Return a configured logger for a module.
    """

    logger = logging.getLogger(module_name)

    # Prevent duplicate handlers
    if not logger.handlers:

        logger.setLevel(logging.INFO)

        log_name = module_name.replace(".", "_")

        log_file = LOG_DIR / f"{log_name}.log"

        file_handler = logging.FileHandler(log_file)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
