from typing import Optional
from fastapi import HTTPException
from openai.error import OpenAIError
from utils.logger import logger  # Assuming logger is defined in utils/logger.py 

class OpenAIError(HTTPException):
    """
    Custom exception class for errors related to the OpenAI API.

    Attributes:
        status_code (int): HTTP status code for the error.
        detail (str): Detailed error message.
    """
    def __init__(self, detail: str = "OpenAI API error", **kwargs: dict):
        super().__init__(status_code=500, detail=detail, **kwargs)

class InvalidRequestError(HTTPException):
    """
    Custom exception class for errors related to invalid user requests.

    Attributes:
        status_code (int): HTTP status code for the error.
        detail (str): Detailed error message.
    """
    def __init__(self, detail: str = "Invalid request", **kwargs: dict):
        super().__init__(status_code=400, detail=detail, **kwargs)

class DatabaseError(HTTPException):
    """
    Custom exception class for errors related to database operations.

    Attributes:
        status_code (int): HTTP status code for the error.
        detail (str): Detailed error message.
    """
    def __init__(self, detail: str = "Database error", **kwargs: dict):
        super().__init__(status_code=500, detail=detail, **kwargs)