from typing import Dict, Optional
import datetime
import jwt
from config.settings import SECRET_KEY  # Import the secret key for JWT signing

def create_token(user_id: str) -> str:
    """
    Creates a new JWT token for the given user ID.

    Args:
        user_id (str): The user ID to be included in the token.

    Returns:
        str: The generated JWT token.
    """
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Set token expiration time
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")  # Use HS256 algorithm for signing

def decode_token(token: str) -> Optional[str]:
    """
    Decodes the given JWT token and returns the user ID if the token is valid, otherwise returns None.

    Args:
        token (str): The JWT token to be decoded.

    Returns:
        Optional[str]: The user ID extracted from the token, or None if the token is invalid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])  # Use HS256 algorithm for verification
        return payload["user_id"]
    except jwt.exceptions.InvalidTokenError:
        return None