import logging
import logging.handlers
import os

# Create a logs directory if it doesn't exist
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Path for the log file
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Create a logger object
logger = logging.getLogger("FinanceAppLogger")

# Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger.setLevel(logging.INFO)

# Create a formatter for all handlers
formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# Console Handler: prints logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# File Handler: writes logs to a file, rotating when it reaches 1MB
file_handler = logging.handlers.RotatingFileHandler(
    LOG_FILE, maxBytes=1_000_000, backupCount=5, encoding="utf-8"
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def log_info(message: str):
    """Logs an informational message."""
    logger.info(message)


def log_warning(message: str):
    """Logs a warning message."""
    logger.warning(message)


def log_error(message: str):
    """Logs an error message."""
    logger.error(message, exc_info=True)


def log_debug(message: str):
    """Logs a debug message."""
    logger.debug(message)


# Example usage:
# log_info("Application started.")
# log_warning("Low disk space.")
# try:
#     1 / 0
# except ZeroDivisionError:
#     log_error("An error occurred.")
# log_debug("This is a debug message.")
