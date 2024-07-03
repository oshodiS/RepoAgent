# repo_agent/log.py
import logging
import sys

from loguru import logger
from repo_agent.log import logger

logger = logger.opt(colors=True)
"""
RepoAgent logger object.

Default settings:
- Format: `[%(asctime)s %(name)s] %(levelname)s: %(message)s`
- Level: `INFO`, can be changed based on the `CONFIG["log_level"]` configuration
- Output: stdout

Usage example:
    ```python
    
    # Basic message logging
    logger.info("It <green>works</>!") # Using colors

    # Logging exception information
    try:
        1 / 0
    except ZeroDivisionError:
        # Using `logger.exception` automatically appends the exception's stack trace information when logging exception messages.
        logger.exception("ZeroDivisionError occurred")

    # Logging debug information
    logger.debug("Debugging info: {}", some_debug_variable)

    # Logging warning messages
    logger.warning("This is a warning message")

    # Logging error messages
    logger.error("An error occurred")

    # Using the native print function (redirected to logger)
    print("This will be logged as an INFO level message")
    ```
"""


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where the logged message originated
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__: # type: ignore
            frame = frame.f_back # type: ignore
            depth += 1

        # Log to Loguru
        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def set_logger_level_from_config(log_level):

    logger.remove()
    logger.add(sys.stderr, level=log_level)

    # Intercept standard logging
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    logger.success(f"Log level set to {log_level}!")


