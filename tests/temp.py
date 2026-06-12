import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from app.logger_manager import LoggerManager

logger = LoggerManager()

logger.log_info("Application started")
logger.log_warning("Memory usage high")
logger.log_error("Database connection failed")