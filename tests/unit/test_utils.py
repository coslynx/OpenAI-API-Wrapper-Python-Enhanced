import pytest
from utils.logger import get_logger
from utils.exceptions import OpenAIError, InvalidRequestError, DatabaseError

@pytest.fixture
def logger():
    """Provides a logger instance for testing."""
    return get_logger()

def test_logger_info(logger, caplog):
    """Tests logging at INFO level."""
    logger.info("This is an info message.")
    assert "This is an info message." in caplog.text

def test_logger_error(logger, caplog):
    """Tests logging at ERROR level."""
    logger.error("This is an error message.")
    assert "This is an error message." in caplog.text

def test_openai_error(mocker):
    """Tests handling OpenAIError."""
    mocker.patch("openai.OpenAI.completions.create", side_effect=OpenAIError("OpenAI error"))
    from routes.generate_text import generate_text
    with pytest.raises(OpenAIError) as exc_info:
        generate_text(request=None, openai=None)
    assert "OpenAI error" in str(exc_info.value)

def test_invalid_request_error(mocker):
    """Tests handling InvalidRequestError."""
    mocker.patch("openai.OpenAI.completions.create", side_effect=InvalidRequestError("Invalid request"))
    from routes.generate_text import generate_text
    with pytest.raises(InvalidRequestError) as exc_info:
        generate_text(request=None, openai=None)
    assert "Invalid request" in str(exc_info.value)

def test_database_error(mocker):
    """Tests handling DatabaseError."""
    mocker.patch("database.database.get_db", side_effect=DatabaseError("Database error"))
    from routes.generate_text import generate_text
    with pytest.raises(DatabaseError) as exc_info:
        generate_text(request=None, openai=None, db=None)
    assert "Database error" in str(exc_info.value)