"""Create a logger for app-related events (bugs, info, etc)

For more advanced uses, see https://realpython.com/python-logging/"""

import logging
import logging.handlers
import os

import dotenv

dotenv.load_dotenv()

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv("DEBUG_LEVEL", "WARNING"))

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.handlers.TimedRotatingFileHandler(
    "logs/app.log", "midnight"
)
c_handler.setLevel(os.getenv("DEBUG_LEVEL", "WARNING"))
f_handler.setLevel(os.getenv("DEBUG_LEVEL", "WARNING"))

# Create formatters and add it to handlers
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
