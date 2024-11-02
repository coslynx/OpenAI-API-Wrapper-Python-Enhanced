import logging
import os
from config.settings import LOG_LEVEL  # Potentially import logging level

def get_logger(name=__name__):
    """Retrieves the logger instance for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)  # Set the logging level if defined

    # Configure the logger handler (Console or File)
    if os.getenv("LOG_FILE"): 
        file_handler = logging.FileHandler(os.getenv("LOG_FILE"))
        logger.addHandler(file_handler)
    else: 
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)
    
    # Format the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    if os.getenv("LOG_FILE"): 
        file_handler.setFormatter(formatter)

    return logger