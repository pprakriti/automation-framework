import logging
import os

def get_logger():

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("automation-framework")

    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(
            "logs/test.log"
            )

        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger