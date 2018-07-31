import logging
import os


def setup():
    logger = logging.getLogger("q_logger")
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] %(name)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(os.getenv("LOGLEVEL", "INFO"))
    return logger


logger = setup()
