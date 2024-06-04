import logging
from .config import settings


logger = logging.getLogger("api")
logger.setLevel(settings.LOG_LEVEL)
file_handler = logging.FileHandler("latest.log")
stream_handler = logging.StreamHandler()

formatter = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s]: %(message)s")

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)